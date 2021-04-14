from termcolor import colored
import requests
from rich.console import Console
import sys as sys

from .error import SearchError
from .save import SaveSearchResults
from .markdown import MarkdownRenderer

# Required for OAuth
import json
from oauthlib.oauth2 import MobileApplicationClient
from requests_oauthlib import OAuth2Session

# Required for Selenium script and for web_driver_manager
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

console = Console()


class Utility():
    def __init__(self):
        # the parent url
        self.search_content_url = "https://api.stackexchange.com/"

    def __get_search_url(self, question, tags):
        """
        This function returns the url that contains all the custom
        data provided by the user such as tags and question, which
        can finally be used to get answers
        """
        return f"{self.search_content_url}/2.2/search/advanced?order=desc&sort=relevance&tagged={tags}&title={question}&site=stackoverflow"

    def make_request(self, que, tag: str):
        """
        This function uses the requests library to make the rest api call to the stackexchange server.

        :param que: The user questions that servers as a question in the api.
        :type que: String
        :param tag: The tags that user wants for searching the relevant answers. For e.g. TypeError might be for multiple languages so is tag is used as "Python" then the api will return answers based on the tags and question.
        :type tag: String
        :return: Json response from the api call.
        :rtype: Json format data
        """
        print("\U0001F50E Searching for the answer")
        try:
            resp = requests.get(self.__get_search_url(que, tag))
        except:
            SearchError("\U0001F613 Search Failed", "\U0001F4BB Try connecting to the internet")
            sys.exit()
        return resp.json()

    def get_que(self, json_data):
        """
        This function returns the list of ids of the questions
        that have been answered, from the response that we get
        from the make_request function.
        """
        que_id = []
        for data in json_data['items']:
            if data["is_answered"]:
                que_id.append(data["question_id"])
        return que_id

    def get_ans(self, questions_list):
        """
        This function prints the answer to the queries
        (question and tags) provided by the user. It does so
        in the following manner :
        
        1) Takes in account only th first question id from the
        list of question ids
        
        2) Tries to get a response from the url obtained by appending
        question id to the search_content_url variable
        
        3) Use the data received from the above request and loop
        through it to print the answer 
        """
        ans = []
        for questions in range(1):
            try:
                resp = requests.get(
                    f"{self.search_content_url}/2.2/questions/{questions_list[questions]}/answers?order=desc&sort=votes&site=stackoverflow&filter=!--1nZwsgqvRX"
                )
            except:
                SearchError("\U0001F613 Search Failed", "\U0001F4BB Try connecting to the internet")
                sys.exit()
            json_ans_data = resp.json()

            for data in json_ans_data["items"]:
                output_content = [
                    colored(
                        "--------------------------------------------------------",
                        'red'), data["body_markdown"],
                    f"\U0001F517 Link to the answer:{data['link']}"
                ]

                for output_index, output_text in enumerate(output_content):
                    """
                    Loop through the output_text and print the element
                    if it the last one, the text[0] is printed
                    along with text[-1]

                    if text is markdown , render the markdown
                    """
                    if output_index == len(output_content) - 1:
                        console.print(output_text)

                        console.print(output_content[0])
                        break

                    if output_index == len(output_content) - 2:
                        renderer = MarkdownRenderer(output_text)

                        continue

                    console.print(output_text)
            ans.append(json_ans_data["items"])
        return ans

    # Get an access token and extract to a JSON file "access_token.json"
    @classmethod
    def setCustomKey(self):
        client_id = 20013

        # scopes possible values:
        # read_inbox - access a user's global inbox
        # no_expiry - access_token's with this scope do not expire
        # write_access - perform write operations as a user
        # private_info - access full history of a user's private actions on the site
        scopes = 'read_inbox'

        authorization_url = 'https://stackoverflow.com/oauth/dialog'
        redirect_uri = 'https://stackexchange.com/oauth/login_success'

        # Create an OAuth session and open the auth_url in a browser for the user to authenticate
        stackApps = OAuth2Session(client=MobileApplicationClient(client_id=client_id), scope=scopes, redirect_uri=redirect_uri)
        auth_url, state = stackApps.authorization_url(authorization_url)

        # Try to install web drivers for one of these browsers
        # Chrome, Firefox, Edge (One of them must be installed)
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
        except ValueError:
            try:
                driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            except ValueError:
                try:
                    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
                except ValueError:
                    print("You do not have one of these supported browsers: Chrome, Firefox, Edge")

        # Open auth_url in one of the supported browsers
        driver.get(auth_url)

        # Close the window after 20s (Assuming that the user logs in within 30 seconds)
        time.sleep(30)
        # Close the windows as soon as authorization is done
        try:
            WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.TAG_NAME, "h2"))
            )
            callback_url = driver.current_url
        finally:
            driver.quit()

        # Extract access token data from callback_url
        accessTokenData = stackApps.token_from_fragment(callback_url)

        # Store the access token data in a dictionary
        jsonDict = {
            "access_token": accessTokenData['access_token'],
            "expires": accessTokenData['expires'],
            "state": state
        }

        with open('access_token.json', 'w') as jsonFile:
            json.dump(jsonDict, jsonFile)