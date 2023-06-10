#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row[:-1]:
            print("{:d}".format(num), end=' ')
        if len(row) > 0:
            print("{:d}".format(row[-1]))
        else:
            print()
