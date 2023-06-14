#!/usr/bin/python3
sq_m = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

nm = sq_m(matrix)
print(nm)
print(matrix)
