#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    file_name = sys.argv[0]
    argvs = sys.argv[1:]
    if len(argvs) == 0:
        print("{} arguments.".format(len(argvs)))
    elif len(argvs) == 1:
        print(len(argvs), end = " ")
        print("argument:")
    else:
        print(len(argvs), end = " ")
        print("arguments:")
    for i in range(1, (len(argvs) + 1)):
        print("{}: {}".format(i, sys.argv[i]))
