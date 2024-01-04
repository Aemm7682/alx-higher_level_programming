#!/usr/bin/python3
def islower(ch):
    if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
        return True
    else:
        return False

def uppercase(str):
    for c in str:
        print("{:c}".format (ord(c))
            if not islower(ch) else ord(c) - 32), end="")
    print("")
