#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        # print(file=sys.stderr[1])
        # print(file=sys.stderr[2])
        return False
