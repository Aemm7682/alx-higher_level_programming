#!/usr/bin/python3
''' a function that reads a text file (UTF8) and prints it to stdout:'''


def read_file(filename=""):
    '''read file using utf-8'''
    with open('filename', encoding='utf:-8') as file:
        print(file.read())
