#!/usr/bin/python3
'''function that returns an object
(Python data structure) represented
by a JSON string:'''


import json


def from_json_string(my_str):
    '''
    this program to change from string to dic again
    Argument:
        my_str: is the string to be changed to dict
    return: the dict value
    '''
    return json.loads(my_str)
