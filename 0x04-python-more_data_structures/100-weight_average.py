#!/usr/bin/python3
"""Write a function that returns the weighted average of all integers tuple"""


def weight_average(my_list=[]):
    avg = 0
    num = 0
    if my_list is None:
        return 0
    for tup in my_list:
        avg += (tup[0] * tup[1])
        num += tup[1]
    result = avg / num

    return result
