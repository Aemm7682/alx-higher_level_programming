#!/usr/bin/python3
'''a function that writes a string to
a text file (UTF8) and returns the
number of characters written: '''


def write_file(filename="", text=""):
    '''write with UTF8
    Argment:
        filename: is the file
        text: text to be write
        num_char: the char count
        return: return the number of char
        '''
    with open(filename, 'w', encoding='utf-8') as file:
        num_char = file.write(text)
    return num_char
