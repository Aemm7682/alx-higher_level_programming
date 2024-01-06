#!/usr/bin/python3
import sys
file_name = sys.argv[0]
argvs = sys.argv[1:]
print(len(argvs), end = " ")
print("arguments:")
for i in range(1, (len(argvs) + 1)):
    print("{}: {}".format(i, sys.argv[i]))
