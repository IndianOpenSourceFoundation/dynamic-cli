#!/usr/bin/env python
import argparse
from lol.prompt import Prompt
from termcolor import colored
from src.arguments.utility import Utility
import sys as sys


class SearchError():
    def __init__(self, error_statement, suggestion):
        self.error_statement = error_statement
        self.suggestion = suggestion

        self.evoke_search_error(self.error_statement)

    def evoke_search_error(self, error_statement):
        print_text = [colored(error_statement, 'red'), colored(self.suggestion, 'green')]
        for text_to_print in print_text:
            print(text_to_print)

class Search():
    def __init__(self, arguments):
        self.arguments = arguments
        self.utility_object = Utility()


    def search_args(self):
        if self.arguments.search:
            queries = [
                "What do you want to search",
                "Tags"
            ]
            query_solutions = []
            
            for each_query in queries:
                try:
                    prompt = Prompt(str(each_query)).prompt()
                except:
                    sys.exit()

                query_solutions.append(prompt)

            question, tags = query_solutions[0], query_solutions[1]
            json_output = self.utility_object.make_request(question, tags)
            questions = self.utility_object.get_que(json_output)
            if questions == []:
                search_error = SearchError(
                    "No answer found",
                    "Please try reddit"
                )
            else:
                self.utility_object.get_ans(questions)
