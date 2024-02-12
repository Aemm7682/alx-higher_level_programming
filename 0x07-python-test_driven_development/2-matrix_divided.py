#!/usr/bin/python3
''' function that divides all elements of a matrix.'''


def matrix_divided(matrix, div):
    '''function that divides all elements of a matrix.
    Argument:
        matrix: must be a list of lists of integers or floats
        div: must be a number (integer or float)
    return:
        list: that return the divid matrix
    raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    '''
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix " +
                        "(list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix " +
                            "(list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if type(x) not in (int, float):
                raise TypeError("matrix must be a matrix " +
                                "(list of lists) of integers/floats")

    return [[round(x / div, 2) for x in row] for row in matrix]


if __name__ == "__main__":
    import dectest
    doctest.testfile("test/2-matrix_divided.txt")
