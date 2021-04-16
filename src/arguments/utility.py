from termcolor import colored
import requests
from rich.console import Console
import sys as sys
import os
import time
from collections import defaultdict

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
        1) Gets the details of all the relavant question and stores their title, link and id in "question_data" list. [See line 104]
        2) I have introduced the concept of active question, i.e. , the question whose answer is currently being displayed.
        3) The index of the active question in "question_data" array is stored in "question_posx"
        2) By Default, shows the answer to the first question. Creates an breakable infinite loop asking the user asnwer to which question he wants to see.
        4) The value of "question_posx" changes according to user input, displaying answer to different questions in "questions_data" list.
        3) The answers to the questions requested by the user are stored in cache for faster access time during subsequent calls.
        """
        
        """ Create batch request to get details of all the questions """
        batch_ques_id = ""
        for question_id in questions_list:
            batch_ques_id += str(question_id) + ";"
        print(batch_ques_id)

        try:
            resp = requests.get(
                f"{self.search_content_url}/2.2/questions/{batch_ques_id[:-1]}?order=desc&sort=votes&site=stackoverflow&filter=!--1nZwsgqvRX"
            )
        except:
            SearchError("Search Failed", "Try connecting to the internet")
            sys.exit()
        json_ques_data = resp.json()

        """ Store the received questions data into the following data format 
            list(  list( question_title, question_link, question_id )  )
        """
        questions_data = [[item['title'], item['link'], item['question_id']] for item in json_ques_data["items"] ]

        os.system('cls' if os.name == 'nt' else 'clear')            # Clear terminal

        downloaded_questions_cache = defaultdict(lambda: False)     # cache array to store the requested answers. Format of storage { question_id:[answer_body, answer_link] }
        
        question_posx = 0                                           # Stores the currently showing question index in questions_data
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            console.rule('[bold blue] Relevant Questions', style="bold red")
            for idx, question_data in enumerate(questions_data):                                                # Printing all the questions. The active question is printed GREEN.
                if question_posx == idx:
                    console.print("[green]{}. {}  |  {}".format(idx+1, question_data[0], question_data[1]))
                else:
                    console.print("{}. {}  |  {}".format(idx+1, question_data[0], question_data[1]))

            console.rule("[bold blue] Answer of question {}".format(question_posx+1), style="bold red")
            current_question_id = questions_data[question_posx][2]                                          # Gets the question_id of active question
            if(downloaded_questions_cache[current_question_id]):                                            # Searches for the id in cache. If present then prints it
                output_content = downloaded_questions_cache[current_question_id]
                for output_index, output_text in enumerate(output_content):
                    """
                    Loop through the output_text and print the element
                    if it the last one, the text[0] is printed
                    along with text[-1]

                    if text is markdown , render the markdown
                    """
                    if output_index == len(output_content) - 1:
                        console.print("Link to the answer: " + output_text)
                        break

                    if output_index == len(output_content) - 2:
                        MarkdownRenderer(output_text)
                        continue

                    console.print(output_text)

            else:                                                                                       # If the cache has no entry for the said question id, the downloads the answer 
                try:                                                                                    # and makes an entry for it in the said format [Line 110] and restarts the loop.
                    resp = requests.get(
                        f"{self.search_content_url}/2.2/questions/{current_question_id}/answers?order=desc&sort=votes&site=stackoverflow&filter=!--1nZwsgqvRX"
                    )
                except:
                    SearchError("Search Failed", "Try connecting to the internet")
                    sys.exit()
                json_ans_data = resp.json()
                print(json_ans_data["items"])
                most_upvoted = json_ans_data["items"][0]
                downloaded_questions_cache[current_question_id] = [most_upvoted["body_markdown"], most_upvoted['link']]
                del most_upvoted
                continue

            console.rule("[bold blue]", style="bold red", align="right")
            while True:                           
                posx = int(input("Enter the question number you want to view (Press 0 to quit): ")) - 1     # Asks the user for next question number. Makes it the active question and loop restarts
                if (posx == -1):                                                                            # Press 0 to exit
                    return
                elif (0<=posx<len(questions_data)):
                    question_posx = posx
                    break
                else:
                    console.print("Please enter a valid question number")
                    continue

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