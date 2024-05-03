#!/usr/bin/python3
"""
each interior number is the sum of the
two numbers above it in the triangle (from the previous row).
It does this until it has generated n rows.
"""


def pascal_triangle(n):
    """function to creat pascal triangle
    Args:
        n (int): number of rows
        triangle (list): pascal triangle
        row (list): row of pascal triangle
        i (int): index of row
        j (int): index of row
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
