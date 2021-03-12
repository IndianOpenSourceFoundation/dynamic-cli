#!/usr/bin/env python
import argparse
from termcolor import colored
from .utility import Utility
from .reddit import reddit
import getpass

PARSER = argparse.ArgumentParser()
PARSER.add_argument(
    "-s", "--search", help="enable debug mode", action="store_true")

ARGV = PARSER.parse_args()
utility_obj = Utility()
reddit_obj = reddit()


class Search:

    def search_args(self):
        if ARGV.search:
            print("What do you want to search - ", end=" ")
            question = input()
            print("Tags : ", end=" ")
            tags = input()
            json_output = utility_obj.make_request(question, tags)
            questions = utility_obj.get_que(json_output)
            if questions == []:
                print(colored('No answer found,', 'red'),
                      colored('searching on reddit', 'green'))
               
                val=reddit_obj.getjson(question)
                reddit_obj.getdata(val)

            else:
                utility_obj.get_ans(questions)
