#!/usr/bin/python3
'''function that returns the dictionary description with
simple data structure (list, dictionary, string, integer
and boolean) for JSON serialization of an object'''


def class_to_json(obj):
    '''
    using json
    The function then returns the result of calling 
    the __dict__ method on the object. __dict__ is a 
    special method that returns a dictionary containing 
    the object's attributes and their values.
    '''
    return obj.__dict__
