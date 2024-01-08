#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for submatrix in matrix:
        if len(submatrix) == 0:
            print()
        for i in range(len(submatrix)):
            print("{:d}".format(submatrix) ,
                    end="\n" if i i is len(submatrix) -a  else " ")
