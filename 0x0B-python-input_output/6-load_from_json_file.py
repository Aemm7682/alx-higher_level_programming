#!/usr/bin/python3
'''a function that creates an Object from a “JSON file'''


import json


def load_from_json_file(filename):
    '''
    this program to deserialization from string
    to dict again
    Argument:
        filename: is the file to load from
    '''
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
