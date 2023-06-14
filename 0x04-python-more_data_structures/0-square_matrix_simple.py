#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = matrix.copy()
    return [[num ** 2 for num in row] for row in my_matrix]
