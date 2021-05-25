import os

from .utility import get_browser_driver
from .settings import LOGIN_PATH
from .settings import TOKEN_FILE_PATH

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_token_from_cookie(cookie, token):
    for el in cookie:
        if el['name'] == token:
            return el

def get_token_from_file():
    try:
        with open(TOKEN_FILE_PATH, 'r') as f:
            data = f.read()
    except Exception as e:
        print(e)
    if(not data or data==""):
        raise RuntimeError("Token not found in file")
    else:
        return data

def get_cookies_from_login():

    """Capture browser cookies for authentication

    Provides the user browser window to login to Notion
    Returns the user's cookies which can be used to
    access and transfer content to user's Notion account
    """
    driver = get_browser_driver()
    try:
        driver.get(LOGIN_PATH)
        WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.CLASS_NAME,
                                            "notion-sidebar-container")))
        return driver.get_cookies()
    except Exception as e:
        print(e)
    finally:
        driver.quit()

class NotionClient():
    """

    Implements Login and token retrieval

    Handles the entire procedure of connecting to User's Notion account,
    generating Notion's tokenv2_cookie, storing it locally and uploading
    content to User's space
    """
    def __init__(self):
        """
        No input parameters required for instatiating object.
        tokenv2_cookie stores the cookie containing user's tokenv2
        tokenv2_key is used to create environment variable
        """
        self.tokenv2_cookie = None
        self.tokenv2_key = 'TOKENV2'

    def save_token_file(self):
        if(self.tokenv2_cookie):
            with open(TOKEN_FILE_PATH, 'w') as f:
                f.write(str(self.tokenv2_cookie))

    def get_tokenv2_cookie(self):
        # Sets 'tokenv2_cookie equal to the particular cookie containing token_v2
        if not self.tokenv2_cookie:
            try:
                self.tokenv2_cookie = get_token_from_file()
            except Exception:
                try:
                    cookies = get_cookies_from_login()
                    self.tokenv2_cookie = get_token_from_cookie(cookies, 'token_v2')
                except Exception as e:
                    print(e)
                    self.tokenv2_cookie = None
                finally:
                    if self.tokenv2_cookie:
                        os.environ[self.tokenv2_key] = str(self.tokenv2_cookie)
                        self.save_token_file()
                    else:
                        raise RuntimeError("Cookie unreachable")
        return self.get_tokenv2_cookie