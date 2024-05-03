#!/usr/bin/python3
"""
Write a function that inserts a line of text to 
a file, after each line containing a specific 
string (see example):"""


def append_after(filename="", search_string="", new_string=""):
    """
    function to append a line of text to a file
    Args:
        filename (str): file name
        search_string (str): string to search for
        new_string (str): string to append
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            if search_string in line:
                f.write(line + new_string)
            else:
                f.write(line)
