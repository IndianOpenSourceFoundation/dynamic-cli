#!/usr/bin/env python

import argparse
from src.arguments.search import Search

version = "0.1"

parser = argparse.ArgumentParser()
parser.add_argument("-s",
                    "--search",
                    help="enable debug mode",
                    action="store_true")

parser.add_argument("-V",
                    "--version",
                    version=f"Dynamic-CLI version {version}",
                    action='version')

parser.add_argument(
    "-n",
    "--new",
    help="Opens browser to create new Stack Overflow question.",
    const=True,
    metavar="title (optional)",
    nargs="?")

ARGV = parser.parse_args()

search_flag = Search(ARGV)

if __name__ == "__main__":
    search_flag.search_args()
