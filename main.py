#!/usr/bin/env python

import argparse
from src.arguments.search import Search


version = "0.1.0"

parser = argparse.ArgumentParser()
parser.add_argument("-st",
                    "--start",
                    help="introduce you to dynamic",
                    action="store_true")

parser.add_argument("-s",
                    "--search",
                    help="search a question on StackOverflow",
                    action="store_true")

parser.add_argument("-V","-v",
                    "--version",
                    version=f"Dynamic-CLI version {version}",
                    action='version')


parser.add_argument(
    "-n",
    "--new",
    help="Opens browser to create new StackOverflow question.",
    const=True,
    metavar="title (optional)",
    nargs="?")

parser.add_argument("-file",
                    "--file",
                    help="Save answer to a file",
                    action="store_true")

parser.add_argument("-c",
                    "--custom",
                    help="Set a custom API key",
                    action="store_true")

parser.add_argument("-u",
                    "--update",
                    help="Check updates for the application",
                    action="store_true")

parser.add_argument("-GET",
                    help="Make a GET request to an API",
                    action='store_true')

parser.add_argument("-p",
                    "--playbook",
                    help="View and organise the playbook",
                    action='store_true')

ARGV = parser.parse_args()

search_flag = Search(ARGV)

if __name__ == "__main__":
    if ARGV.start:
        print('''
        \U0001F604 Hello and Welcome to Dynamic CLI 
        Use the following commands to get started 
        \U0001F50E to search StackOverflow, type  'dynamic -s' 
        \U0001F4C4 to create a new StackOverflow question in the Website, type 'dynamic -n [title(optional)]' 
        \U0001F4C2 to save answer inside a file, type 'dynamic -file'
        \U00002728 to know the Version, type 'dynamic -V' or 'dynamic -v' 
        \U0001F609 to restart, type 'dynamic -st'
        \U00002755 to get help, type 'dynamic -h'
        ''')
    else:
        search_flag.search_args()