#!/usr/bin/python3
'''Defining to_json_string function'''


from json import dumps


def to_json_string(my_obj):
    '''Returns json representation of an object'''
    return dumps(my_obj)
