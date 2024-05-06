#!/usr/bin/python3
"""a function that prints a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    Argument:
    text: is str
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    sando = ['?', ':', '.']
    for delim in sando:
        text = text.replace(delim, delim + "\n\n")
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("test/5-text_indentation.txt")
