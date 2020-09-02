#!/usr/bin/env python
import argparse
from termcolor import colored
from .utility import Utility

PARSER = argparse.ArgumentParser()
PARSER.add_argument(
    "-s", "--search", help="enable debug mode", action="store_true")

ARGV = PARSER.parse_args()
utitlity_obj = Utility()


class Search:

    def search_args(self):
        if ARGV.search:
            print("What do you want to search - ", end=" ")
            question = input()
            print("Tags : ", end=" ")
            tags = input()
            json_output = utitlity_obj.make_request(question, tags)
            questions = utitlity_obj.get_que(json_output)
            if questions == []:
                print(colored('No answer found,', 'red'),
                      colored('Please try reddit', 'green'))
            else:
                utitlity_obj.get_ans(questions)
