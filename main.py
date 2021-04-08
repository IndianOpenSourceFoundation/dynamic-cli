#!/usr/bin/env python

import argparse
from src.arguments.search import Search

import os
import sys

PARSER = argparse.ArgumentParser()
PARSER.add_argument("-s",
                    "--search",
                    help="enable debug mode",
                    action="store_true")

ARGV = PARSER.parse_args()

search_flag = Search(ARGV)

if __name__ == "__main__":
	if sys.platform.startswith('linux'):
	    euid = os.geteuid()
	    if euid != 0:
		    print ("Script not started as root. Running sudo..")
		    args = ['sudo', sys.executable] + sys.argv + [os.environ]
		    # the next line replaces the currently-running process with the sudo
		    os.execlpe('sudo', *args)

	search_flag.search_args()