#!/usr/bin/python3
'''Defining write_file function with two arguments'''


def number_of_lines(filename=""):
    '''Reads filename with uft-8'''
    with open(filename, "w", encoding='utf-8') as f:
        return f.write((text))
