#!/usr/bin/python3
'''Module for lookup method.'''

def lookup(obj):
    '''Looks yp object attributesand methods.
    Args:
        obj (object): the object to list.

    Returns
    list: the list of available attributes and methods of an object
    '''
    return dir(obj)
