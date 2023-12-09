#!/usr/bin/python3
'''Contains the "class_to_json" function'''
def class_to_json(obj):
    '''All attributes of the obj Class are serializable:
        list, dictionary, string, integer and boolean'''
    return obj.__dict__
