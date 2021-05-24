import os
import sys

from .utility import Utility
from .error import SearchError

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def get_token_from_cookie(cookie, token):
    for el in cookie:
        if el['name'] == token:
            return el
    pass

class NotionClient():
    """
    Handles the entire procedure of connecting to User's Notion account,
    generating Notion's tokenv2_cookie, storing it locally and uploading content
    to User's space
    """
    def __init__(self):
        self.tokenv2_cookie = None
        self.base_url = "https://www.notion.so/"
        self.login_path = "login/"
        self.linux_path = "/home/{}/Documents/dynamic".format(os.getenv('USER'))
        self.mac_path = "/Users/{}/Documents/dynamic".format(os.getenv('USER'))
        self.file_name = 'tokenv2_cookie.key'

    def get_token_from_file(self):
        raise FileNotFoundError("File not found")
        return None

    def get_login_path(self):
        return self.base_url + self.login_path

    def save_token_file(self):
        pass

    def get_cookies_from_login(self):
        """
        Provides the user browser window to login to Notion
        Returns the user's cookies which can be used to
        access and transfer content to user's Notion account
        """
        driver = Utility().get_browser_driver()
        try:
            driver.get(self.get_login_path())
            WebDriverWait(driver, 300).until(
                EC.presence_of_element_located((By.CLASS_NAME,
                                                "notion-sidebar-container")))
            return driver.get_cookies()
        except Exception as e:
            print(e)
        finally:
            driver.quit()

    def set_tokenv2_cookie(self):
        # Sets 'tokenv2_cookie equal to the particular cookie containing token_v2
        if not self.tokenv2_cookie:
            try:
                self.tokenv2_cookie = self.get_token_from_file()
            except:
                try:
                    cookies = self.get_cookies_from_login()
                    self.tokenv2_cookie = get_token_from_cookie(cookies, 'token_v2')
                except Exception as e:
                    print(e)
                    self.tokenv2_cookie = None
                finally:
                    os.environ['tokenv2_cookie'] = self.tokenv2_cookie
                    if self.tokenv2_cookie:
                        self.save_token_file()