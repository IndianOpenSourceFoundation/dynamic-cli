from termcolor import colored
import requests
from rich.console import Console
from rich.markdown import Markdown
import sys as sys

# Required for Questions Panel
import os
import time
import locale
from collections import defaultdict
from simple_term_menu import TerminalMenu
import webbrowser

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

class Playbook():
    def __init__(self):
        self.linux_path = "/home/{}/Documents/dynamic".format(os.getenv('USER'))
        self.mac_path = "/Users/{}/Documents/dynamic".format(os.getenv('USER'))
        self.file_name = 'dynamic_playbook.json'

    @property
    def playbook_path(self):
        if(sys.platform=='linux'):
            return os.path.join(self.linux_path, self.file_name)
        if(sys.platform=='darwin'):
            return os.path.join(self.mac_path, self.file_name)

    @property
    def playbook_template(self):
        # Basic template and fields of playbook
        return  {"time_of_update": time.time(),"items_stackoverflow":[]}

    @property
    def playbook_content(self):
        # Reads playbook data from local storage and returns it
        try:
            with open(self.playbook_path, 'r') as playbook:
                return json.load(playbook)
        except FileNotFoundError:
            os.makedirs(os.path.dirname(self.playbook_path), exist_ok=True)
            with open(self.playbook_path, 'w') as playbook:
                json.dump(self.playbook_template, playbook, ensure_ascii=False)
            return self.playbook_content

    @playbook_content.setter
    def playbook_content(self, value):
        """
        Saves playbook in the following format
        {   
            time_of_update: unix,
            items_stackoverflow:
            [
                {
                    time: unix timestamp
                    question_id: 123456,
                    question_title: 'question_title',
                    question_link:  'link',
                    answer_body: 'body of the answer'
                },
                ...
            ]
        }
        """
        if type(value) == dict:
            with open(self.playbook_path, 'w') as playbook:
                json.dump(value, playbook, ensure_ascii=False)
            pass
        else:
            raise ValueError("value should be of type dict")

    def is_question_in_playbook(self, question_id):
        content = self.playbook_content
        for entry in content['items_stackoverflow']:
            if int(entry['question_id']) == int(question_id):
                return True
        return False
    
    def add_to_playbook(self, stackoverflow_object, question_id):
        """
        Receives a QuestionsPanelStackoverflow object and 
        saves data of a particular question into playbook
        """
        if self.is_question_in_playbook(question_id):
            SearchError("Question is already in the playbook", "No need to add")
            return
        for question in stackoverflow_object.questions_data:
            if(int(question[1])==int(question_id)):
                content = self.playbook_content
                now = time.time()
                content['time_of_update'] = now
                content['items_stackoverflow'].append({
                    'time_of_creation': now,
                    'question_id': int(question_id),
                    'question_title': question[0],
                    'question_link': question[2],
                    'answer_body': stackoverflow_object.answer_data[int(question_id)]
                })
                self.playbook_content = content

    def delete_from_playbook(self, stackoverflow_object, question_id):
        content = self.playbook_content
        for i in range(len(content["items_stackoverflow"])):
            if content["items_stackoverflow"][i]["question_id"] == question_id:
                del content["items_stackoverflow"][i]
                break
        self.playbook_content = content
        os.system('cls' if os.name == 'nt' else 'clear')
        self = Playbook()
        self.display_panel()
                    
    def display_panel(self):
        playbook_data = self.playbook_content
        if(len(playbook_data['items_stackoverflow']) == 0):
            SearchError("You have no entries in the playbook", "Browse and save entries in playbook with 'p' key")
            sys.exit()
        question_panel = QuestionsPanelStackoverflow()
        for item in playbook_data['items_stackoverflow']:
            question_panel.questions_data.append( [item['question_title'], item['question_id'], item['question_link']] )
            question_panel.answer_data[item['question_id']] = item['answer_body']
        question_panel.display_panel(playbook=True)

class QuestionsPanelStackoverflow():
    def __init__(self):
        self.questions_data = []                        # list(  list( question_title, question_id, question_link )...  )
        self.answer_data = defaultdict(lambda: False)   # dict( question_id:list( body, link )) corresponding to self.questions_data
        self.line_color = "bold red"
        self.heading_color = "bold blue"
        self.utility = Utility()
        self.playbook = Playbook()

    def populate_question_data(self, questions_list):
        """
        Function to populate question data property
        Creates batch request to stackexchange API and to get question details of
        questions with id in the list. Stores the returned data data in the following format:
            list(  list( question_title, question_link, question_id )  )
        """
        with console.status("Getting the questions..."):
            try:
                resp = requests.get(
                    self.utility.get_batch_ques_url(questions_list)
                )
            except:
                SearchError("Search Failed", "Try connecting to the internet")
                sys.exit()
        json_ques_data = resp.json()
        self.questions_data = [[item['title'].replace('|',''), item['question_id'], item['link']] for item in json_ques_data["items"]]

    def populate_answer_data(self, questions_list):
        """
        Function to populate answer data property
        Creates batch request to stackexchange API to get ans of questions with
        question id in the list. Stores the returned data data in the following format:
            dict( question_id:list( body, link ) )
        """
        with console.status("Searching answers..."):
            try:
                resp = requests.get(
                    self.utility.get_batch_ans_url(questions_list)
                )
            except:
                SearchError("Search Failed", "Try connecting to the internet")
                sys.exit()
            json_ans_data = resp.json()
            for item in json_ans_data["items"]:
                if not(self.answer_data[item['question_id']]):
                    self.answer_data[item['question_id']] = item['body_markdown']
        # Sometimes the StackExchange API fails to deliver some answers. The below code is to fetch them
        failed_ques_id = [question[1] for question in self.questions_data if not(self.answer_data[question[1]])]
        if not(len(failed_ques_id) == 0):
            self.populate_answer_data(failed_ques_id)

    def return_formatted_ans(self, ques_id):
        # This function uses uses Rich Markdown to format answers body.
        body_markdown = self.answer_data[int(ques_id)]
        body_markdown = str(body_markdown)
        xml_markup_replacement = [("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", "\""), ("&apos;", "\'"), ("&#39;", "\'")]
        for convert_from, convert_to in xml_markup_replacement:
            body_markdown = body_markdown.replace(convert_from, convert_to)
        width = os.get_terminal_size().columns
        console = Console(width=width-4)
        markdown = Markdown(body_markdown, hyperlinks=False)
        with console.capture() as capture:
            console.print(markdown)
        highlighted = capture.get()
        if locale.getlocale()[1] !='UTF-8':
            box_replacement = [("─", "-"), ("═","="), ("║","|"), ("│", "|"), ('┌', '+'), ("└", "+"), ("┐", "+"), ("┘", "+"), ("╔", "+"), ("╚", "+"), ("╗","+"), ("╝", "+"), ("•","*")]
            for convert_from, convert_to in box_replacement:
                highlighted = highlighted.replace(convert_from, convert_to)
        return highlighted

    def navigate_questions_panel(self, playbook=False):
        # Code for navigating through the question panel
        (message, instructions, keys) = ('Playbook Questions', ". Press 'd' to delete from playbook", ('enter', 'd')) if(playbook) else ('Relevant Questions', ". Press 'p' to save in playbook", ('p', 'enter'))
        console.rule('[bold blue] {}'.format(message), style="bold red")
        console.print("[yellow] Use arrow keys to navigate. 'q' or 'Esc' to quit. 'Enter' to open in a browser" + instructions)
        console.print()
        options = ["|".join(map(str, question)) for question in self.questions_data]
        question_menu = TerminalMenu(options, preview_command=self.return_formatted_ans, preview_size=0.75, accept_keys=keys)
        quitting = False
        while not(quitting):
            options_index = question_menu.show()
            try:
                question_link = self.questions_data[options_index][2]
            except Exception:
                return sys.exit() if playbook else None
            else:
                if(question_menu.chosen_accept_key == 'enter'):
                    webbrowser.open(question_link)
                elif(question_menu.chosen_accept_key == 'p'):
                    self.playbook.add_to_playbook(self, self.questions_data[options_index][1])
                elif(question_menu.chosen_accept_key == 'd' and playbook):
                    self.playbook.delete_from_playbook(self, self.questions_data[options_index][1])

    def display_panel(self, questions_list=[], playbook=False):
        if len(questions_list) != 0:
            self.populate_question_data(questions_list)
            self.populate_answer_data(questions_list)
        self.navigate_questions_panel(playbook=playbook)

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

    def get_batch_ques_url(self, ques_id_list):
        """
        Returns URL which contains ques_ids which can be use to get
        get the details of all the corresponding questions
        """
        batch_ques_id = ""
        for question_id in ques_id_list:
            batch_ques_id += str(question_id) + ";"
        return f"{self.search_content_url}/2.2/questions/{batch_ques_id[:-1]}?order=desc&sort=votes&site=stackoverflow&filter=!--1nZwsgqvRX"

    def get_batch_ans_url(self, ques_id_list):
        batch_ques_id = ""
        for question_id in ques_id_list:
            batch_ques_id += str(question_id) + ";"
        return f"{self.search_content_url}/2.2/questions/{batch_ques_id[:-1]}/answers?order=desc&sort=votes&site=stackoverflow&filter=!--1nZwsgqvRX"

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
        with console.status("Searching..."):
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
        This Function creates QuestionsPanel_stackoverflow class which supports
        Rendering, navigation, searching and redirecting capabilities
        """
        stackoverflow_panel = QuestionsPanelStackoverflow()
        stackoverflow_panel.display_panel(questions_list)
        # Support for reddit searching can also be implemented from here

    def display_playbook(self):
        playbook = Playbook()
        playbook.display_panel()

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