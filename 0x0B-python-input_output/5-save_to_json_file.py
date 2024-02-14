#!/usr/bin/python3
'''a function that writes an Object to
a text file, using a JSON representation:'''


import json


def save_to_json_file(my_obj, filename):
    '''
    this function to serialize and change to
    string and save to file
    Argument:
        my_obj: is the dict
        filename: is the filename
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
