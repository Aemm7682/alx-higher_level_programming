#!/usr/bin/python3
square_matrix_map = \
    __import__('101-square_matrix_map').square_matrix_map

matrix = [[1], [2], [3], [4]]

new_matrix = square_matrix_map(matrix)
print(new_matrix)
print(matrix)
