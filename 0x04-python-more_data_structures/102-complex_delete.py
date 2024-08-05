#!/usr/bin/python3
"""Write a function that deletes keys
with a specific value in a dictionary."""


def complex_delete(a_dictionary, value):
    del_dict = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            del_dict.append(key)

    for key_2 in del_dict:
        del a_dictionary[key_2]

    return a_dictionary
