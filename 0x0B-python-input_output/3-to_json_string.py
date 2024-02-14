#!/usr/bin/python3
'''Write a function that returns the
JSON representation of an object (string):'''


import json


def to_json_string(my_obj):
    '''function to serialize the object by using
    JSON
    Argument:
        my_obj: is the dic'''
    return json.dumps(my_obj)
