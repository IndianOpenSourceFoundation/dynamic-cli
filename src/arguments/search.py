#!/usr/bin/env python
import argparse
import webbrowser
from termcolor import colored
import sys as sys

from .error import SearchError
from .utility import Utility
from .save import SaveSearchResults


class Prompt():
    def __init__(self, message):
        self.message = message

    def prompt(self):
        print(colored(f"{self.message} [?] ", 'cyan'), end='')
        data = input()

        return str(data)


class Search():
    def __init__(self, arguments):
        self.arguments = arguments
        self.utility_object = Utility()

    def search_args(self):
        if self.arguments.search:
            self.search_for_results()
        elif self.arguments.file:
            self.search_for_results(True)
        elif self.arguments.new:
            url = "https://stackoverflow.com/questions/ask"
            if type(self.arguments.new) == str:
                webbrowser.open(f"{url}?title={self.arguments.new}")
            else:
                webbrowser.open(url)

    def search_for_results(self, save=False):
        queries = ["What do you want to search", "Tags"]
        query_solutions = []

        # ask quesiton
        for each_query in queries:
            # Be careful if there are
            # KeyBpard Interupts or EOErrors
            try:
                prompt = Prompt(str(each_query)).prompt()
            except:
                sys.exit()

            query_solutions.append(prompt)

        question, tags = query_solutions[0], query_solutions[1]
        json_output = self.utility_object.make_request(question, tags)
        questions = self.utility_object.get_que(json_output)
        if questions == []:
            # evoke an error
            search_error = SearchError("No answer found", "Please try reddit")
        else:
            data = self.utility_object.get_ans(questions)

            if save:
                filename = SaveSearchResults(data)
                print(
                    colored(f"Answers successfully saved into {filename}",
                            "green"))
