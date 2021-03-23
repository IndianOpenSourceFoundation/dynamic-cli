#!/usr/bin/env python
import argparse
from clint.textui import colored as TextColor
import sys as sys

from .utility import Utility
from .error import SearchError
from .save import SaveSearchResults


class Prompt():
    def __init__(self, message):
        self.message = message

    def prompt(self):
        print(TextColor.cyan(f"{self.message} [?] "), end='')
        data = input()

        return str(data)


class Search():
    def __init__(self, arguments):
        self.arguments = arguments
        self.utility_object = Utility()

    def search_args(self):
        if self.arguments.search:
            self.search_for_answer()
        elif self.arguments.file:
            self.search_for_answer(True)

    def search_for_answer(self, save=False):
        queries = ["What do you want to search", "Tags"]
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
            search_error = SearchError("No answer found", "Please try reddit")
        else:
            data = self.utility_object.get_ans(questions)

            if save:
                SaveSearchResults(data)
