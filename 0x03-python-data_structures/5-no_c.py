#!/usr/bin/env python3
def no_c(my_string):
    w_out = ""
    for i in range(len(my_string)):
        if (my_string[i] != 'c' and my_string[i] !='C'):
            w_out += my_string[i]
    return w_out
