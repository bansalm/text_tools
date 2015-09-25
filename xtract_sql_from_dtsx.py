#!/usr/bin/python
from __future__ import print_function
import sys
import argparse
from argparse import RawTextHelpFormatter
import re
from xml.etree import ElementTree

def process(filename):

    with open(filename, 'rt') as f:
        tree = ElementTree.parse(f)


    print (('-'*80)
           + "\n-- SQL EXPRESSIONS in {filename}\n"
           + ('-'*80).format(filename=filename))
    extract_sql_impressions(tree)

    print (
        "/******************************************************************/")
    print (('-'*80)
       + "\n-- SQL STATEMENTS in {filename}\n"
       + ('-'*80).format(filename=filename))
    extract_sql_statements(tree)


def extract_sql_impressions(tree):
    namespaces = {'DTS': 'www.microsoft.com/SqlServer/Dts'}
    for node in tree.findall('.//DTS:Variable', namespaces):
        for name, value in node.attrib.items():
            if name == '{www.microsoft.com/SqlServer/Dts}Expression'\
                    and value.startswith('"'):
                print (value)
                print ('-'*80)


def extract_sql_statements(tree):
    namespaces = {'DTS': 'www.microsoft.com/SqlServer/Dts'}
    for node in tree.findall('.//DTS:VariableValue', namespaces):
        str = node.text
        if str is not None \
                and (str.lower().find('select') > -1
                    or str.lower().find('insert') > -1
                    or str.lower().find('delete') > -1
                    or str.lower().find('update') > -1
                    or str.lower().find('copy') > -1
                    or str.lower().find('drop') > -1
                    or str.lower().find('truncate') > -1
                    or str.lower().find('grant') > -1
                    or str.lower().find('revoke') > -1
                ) :
            print (node.text)
            print ('-'*80)


def process_command_line_args():
    global args

    epilog = """
This script reads a .dtsx file and extracts all sql statements and
output them to <STDOUT>. """

    parser = argparse.ArgumentParser(description='This script reads .dtsx file '
                                                 ', extracts its SQL  '
                                                 'and writes to <STDOUT>.',
                                     formatter_class=RawTextHelpFormatter,
                                     epilog=epilog)

    parser.add_argument('filename',help='Enter .dtsx filename')

    #parser.add_argument('cols',
    #                    help='Comma delimited column list')

    args = parser.parse_args()


if __name__ == '__main__':
    process_command_line_args()
    process(args.filename)