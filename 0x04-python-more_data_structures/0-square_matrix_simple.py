#!/usr/bin/python3
def square_matrix_simple(my_matrix=[]):
    return list(map(lambda y: list(map(lambda x: x ** 2, y)), my_matrix))
