import requests
import html
from termcolor import colored
from rich.console import Console
from rich.markdown import Markdown
import sys as sys
from keyboard import is_pressed
from os import system, name 

# the rich console
console = Console()

# render markdown text in the terminal
# def print_markdown(markdown):
#     md = Markdown(markdown)
#     console.print(md)


class MarkdownRenderer(object):
    def __init__(self, markdown_text, console_print=True):
        assert isinstance(markdown_text, str), "Expected a string"

        markdown_text = html.unescape(markdown_text)
        self.markdown_text = markdown_text
        self.do_console_print = bool(console_print)

        self.console = Console()  # rich console

        self.render = self.print_mark_down_text()

    def print_mark_down_text(self):
        rendered_markdown = Markdown(self.markdown_text)

        if self.do_console_print:
            self.console.print(rendered_markdown)

        return rendered_markdown

    def __repr__(self):
        return str(self.render)


class SearchError():
    def __init__(self, error_statement, suggestion="Try again"):
        # the error statement
        self.error_statement = error_statement

        # the suggestion statement
        self.suggestion = suggestion

        self.evoke_search_error(self.error_statement)

    def evoke_search_error(self, error_statement):
        print_text = [
            colored(error_statement, 'red'),
            colored(self.suggestion, 'green')
        ]
        for text_to_print in print_text:
            print(text_to_print)


class Utility():

    def __init__(self):
        # the parent url
        self.search_content_url = "https://api.stackexchange.com/"

    def clear(self):
    """ Clear the screen based on the operating system """
    _ = system("cls") if os.name == "nt" else system("clear")

    def __get_search_url(self, question, tags):
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
        print("Searching for the answer")
        try:
            resp = requests.get(self.__get_search_url(que, tag))
        except:
            SearchError("Search Failed", "Try connecting to the internet")
            sys.exit()
        return resp.json()

    def get_que(self, json_data):
        que_id = []
        for data in json_data['items']:
            if data["is_answered"]:
                que_id.append(data["question_id"])
        return que_id

    def get_ans(self, questions_list):
        # ans = []
        for questions in range(1):
            try:
                resp = requests.get(
                    f"{self.search_content_url}/2.2/questions/{questions_list[questions]}/answers?order=desc&sort=votes&site=stackoverflow&filter=!--1nZwsgqvRX"
                )
            except:
                SearchError("Search Failed", "Try connecting to the internet")
                sys.exit()
            json_ans_data = resp.json()

            answers = json_ans_data["items"]
            

            #loop that handles each Answers

            i = 0
            run = True

            while run:

                self.clear()

                print(colored("Use",'red'),colored("Arrow Keys (Up & Down)",'cyan'),colored("to Navigate through",'red'))
                print(colored("Press",'red'),colored("Esc",'cyan'),colored("to Exit",'red'))

                data = answers[i]

                
                output_content = [colored("--------------------------------------------------------",'red'), data["body_markdown"],f"Link to the answer : {data['link']}"]

                console.print('\n'+output_content[0]+'\n')

                for output_index, output_text in enumerate(output_content):
                    """
                    Loop through the output_text and print the element
                    if it the last one, the text[0] is printed
                    along with text[-1]

                    if text is markdown , render the markdown
                    """

                              
                    if output_index == len(output_content) - 1:
                        console.print('\n'+output_content[0])

                        console.print('\n' + output_text + '\n')

                        console.print(output_content[0])
                        break

                    if output_index == len(output_content) - 2:
                        renderer = MarkdownRenderer(output_text)

                        continue


                while True:         #loop that makes navigation through keyboard possible
                    if is_pressed('down'):
                        if(i != len(answers)-1):
                            i = i + 1
                            break
                    if is_pressed('up'):
                        if(i != 0):
                            i = i - 1
                            break
                    if is_pressed('esc'):
                        run = False
                        break
