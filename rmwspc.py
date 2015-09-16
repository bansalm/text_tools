#!/usr/bin/python
from __future__ import print_function
import re


import sys
import argparse
from argparse import RawTextHelpFormatter


def process(replace_string):
    for line in sys.stdin:
        line = re.sub("\t", replace_string, line.rstrip('\n'))
        line = re.sub("  *", replace_string, line)
        print(line.strip())


def process_command_line_args():
    global args

    epilog = """
Examples:
echo -e "\\taman\\t\\t\\t\\tsam\\t" | rmwpsc
"""

    parser = argparse.ArgumentParser(description='This script multiple '
                                                 'tabs/spaces '
                                                 'to single space. Tabs in '
                                                 'the start and end of the '
                                                 'line are also removed',
                                     formatter_class=RawTextHelpFormatter,
                                     epilog=epilog)

    parser.add_argument('--all', dest='replace_tab_with_empty_string'
                        , help='Remove tabs with no space',
                        action="store_true")

    args = parser.parse_args()


if __name__ == '__main__':
    process_command_line_args()
    if (args.replace_tab_with_empty_string):
        process("")
    else:
        process(" ")



