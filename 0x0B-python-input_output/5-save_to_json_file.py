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
    json_string = json.dumps(my_obj)

    with open(filename, 'w') as file:
        file.write(json_string)
