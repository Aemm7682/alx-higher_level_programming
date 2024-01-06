#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    file_name = sys.argv[0]
    argvs = sys.argv[1:]
    len_arg = len(sys.argv) - 1
    if len_arg == 0:
        print("{} arguments.".format(len_arg))
    elif len_arg == 1:
        print(len_arg, end = " ")
        print("argument:")
    else:
        print(len_arg, end = " ")
        print("arguments:")
    for i in range(1, (len_arg + 1)):
        print("{}: {}".format(i, sys.argv[i]))
