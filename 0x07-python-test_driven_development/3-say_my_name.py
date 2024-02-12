#!/usr/bin/python3
'''function to print first and last name'''


def say_my_name(first_name, last_name=""):
    '''function to print first and last name
    argment:
        first_name: first string name
        last_name: last string name
    raise:
        TypeError: first_name or last_name must be a string
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
