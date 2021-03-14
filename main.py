#!/usr/bin/env python

import argparse
from src.arguments.search import Search

PARSER = argparse.ArgumentParser()
PARSER.add_argument("-s",
                    "--search",
                    help="enable debug mode",
                    action="store_true")

ARGV = PARSER.parse_args()

search_flag = Search(ARGV)

if __name__ == "__main__":
    search_flag.search_args()
