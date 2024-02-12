#!/usr/bin/python3
''' this module to add integer '''


def add_integer(a, b=98):
    '''to add two integer
    argument:
        a: is the first int
        b: is the second int with default value 98
    raises:
        TypeError: if a or b is not int
    return:
        the summution of a and b
    '''
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("test/0-add_integer.txt")
