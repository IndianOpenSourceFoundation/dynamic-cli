#!/usr/bin/env python
import argparse
from termcolor import colored
from .utility import Utility


class Search:
    def __init__(self, arguments):
        self.arguments = arguments
        self.utility_object = Utility()


    def search_args(self):
        if self.arguments.search:
            print("What do you want to search - ", end=" ")
            question = input()
            print("Tags : ", end=" ")
            tags = input()
            json_output = utility_obj.make_request(question, tags)
            questions = utility_obj.get_que(json_output)
            if questions == []:
                print(colored('No answer found,', 'red'),
                      colored('Please try reddit', 'green'))
            else:
                utility_obj.get_ans(questions)
