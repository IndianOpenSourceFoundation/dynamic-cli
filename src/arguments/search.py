#!/usr/bin/env python
import argparse
from termcolor import colored
from .utility import Utility, SearchError
import sys as sys

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
                search_error = SearchError("No answer found",
                                           "Please try reddit")
            else:
                self.utility_object.get_ans(questions)
