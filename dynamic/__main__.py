#!/usr/bin/env python

import argparse
from dynamic.namespace import map_arguments
from dynamic.autocomplete import take_input



version = "1.1.0"

parser = argparse.ArgumentParser()


parser.add_argument(
    "-s", "--search", help="search a question on StackOverflow", action="store_true"
)

parser.add_argument(
    "-v", "--version", help="prints version", action="store_true"
)

parser.add_argument(
    "-st", "--start", help="prints starting info", action="store_true"
)




parser.add_argument(
    "-n",
    "--new",
    help="Opens browser to create new StackOverflow question.",
    const=True,
    metavar="title (optional)",
    nargs="?",
)

parser.add_argument(
    "-file", "--file", help="Save answer to a file", action="store_true"
)

parser.add_argument("-c", "--custom", help="Set a custom API key", action="store_true")

parser.add_argument(
    "-u", "--update", help="Check updates for the application", action="store_true"
)

parser.add_argument("-GET", help="Make a GET request to an API", action="store_true")

parser.add_argument("-POST", help="Make a POST request to an API", action="store_true")

parser.add_argument(
    "-DELETE", help="Make a DELETE request to an API", action="store_true"
)

parser.add_argument(
    "-p", "--playbook", help="View and organise the playbook", action="store_true"
)

parser.add_argument(
    "-no",
    "--notion",
    help="\
                    Login to your Notion account to save playbook.\
                    Opens a browser window for you to login to\
                    your Notion accout",
    action="store_true",
)


def main():
    print(
            """\U0001F604 Hello and Welcome to Dynamic CLI
                 \U0001F917 Use the following commands to get started
                 \U0001F50E Search on StackOverflow with 'dynamic -s'
                 \U0001F4C4 Open browser to create new Stack Overflow question with '-n [title(optional)]'
                 \U0001F4C2 Save answer to a file with 'dynamic -file'
                 \U00002728 Know the version of Dynamic CLI with 'dynamic -v'
                 \U0001F609 See this message again with 'dynamic -st'
                 \U00002755 Get help with 'dynamic -h'
                """)
    while 1:
        x = take_input()
        if(x == 'exit'): break
        map_arguments(x)
        

if __name__ == "__main__":
    main()

