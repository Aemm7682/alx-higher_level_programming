#!/usr/bin/python3
"""Write a function that prints a square with the character #."""


def print_square(size):
    """a function that prints a square with the character #.
    Argument:
    size: is integer
    TypeError: size must be an integer
    ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * size + "\n") * size, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("test/4-print_square.txt")
