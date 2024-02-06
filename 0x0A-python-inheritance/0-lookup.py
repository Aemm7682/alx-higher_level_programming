#!/usr/bin/python3
'''module for lookup methods'''


def lookup(obj):
    '''find object and attribute and method
    Args:
            obj: the object list
    Return
        list of attributes
    '''
    return dir(obj)
