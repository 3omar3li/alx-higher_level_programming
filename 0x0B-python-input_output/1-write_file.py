#!/usr/bin/python3
'''Defining write_file function with two arguments'''


def write_file(filename="", text=""):
    '''Reads filename with uft-8'''
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
