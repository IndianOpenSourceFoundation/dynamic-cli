#!/usr/bin/env python
import argparse

PARSER = argparse.ArgumentParser()
# PARSER.add_argument("name", help="name of the person to sort")
PARSER.add_argument("-s", "--search", help="enable debug mode",
                    action="store_true")

ARGV = PARSER.parse_args()


def search_args():
    if ARGV.search:
        print("What do you want to search - ", end=" ")
        question = input()
        return question

