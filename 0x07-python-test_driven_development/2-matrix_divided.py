#!/usr/bin/python3
"""
2-matrix_divided

divide all matrix[2D] numbers by given number
"""

def matrix_divided(matrix, div):
    """
    Divide all matrix[2D] numbers by non-zero number

    Args:
        matrix: 2-Dimenstion(list of lists) of integers of floats
        div: denomenator division

    Return:
        new list of lists of the results of divisions
    """
    new_matrix = [[] * len(matrix)]
    num_col = len(lst[0])
    for lst in matrix:
        if isinstance(lst, list):
            if len(lst) != num_col:
                raise TypeError("Each row of the matrix must have the\
                same size")
        else:
            raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")
    for lst in matrix:
        for num in lst:
            if type(num) is not int or type(num) is not float 
    
