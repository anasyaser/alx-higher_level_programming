#!/usr/bin/python3
"""
2-matrix_divided

divide all matrix[2D] numbers by given number
"""


def list_is_valid(lst):
    """
    Helper function to check validation of list for matrix divide

    Args:
        lst: list to check in
    """
    if isinstance(lst, list):
        return all([(type(num) == int or type(num) == float)
                    for num in lst])
    else:
        return False


def matrix_divided(matrix, div):
    """
    Divide all matrix[2D] numbers by non-zero number

    Args:
        matrix: 2-Dimenstion(list of lists) of integers of floats
        div: denomenator division

    Return:
        new list of lists of the results of divisions
    """
    new_matrix = [[]] * len(matrix)
    err_msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    err_msg2 = "Each row of the matrix must have the same size"
    if not matrix:
        raise TypeError(err_msg1)
    for lst in matrix:
        if not list_is_valid(lst):
            raise TypeError(err_msg1)
        if len(lst) != len(matrix[0]):
            raise TypeError(err_msg2)
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    for i in range(len(matrix)):
        new_matrix[i] = [round(num / div, 2) for num in matrix[i]]

    return new_matrix
