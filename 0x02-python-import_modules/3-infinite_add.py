#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum_all = 0
    file_name = sys.argv[0]
    argvs = sys.argv[1:]
    length = len(sys.argv) - 1
    for i in range(1, length + 1):
        sum_all += int(sys.argv[i])
    print("{}".format(sum_all))
