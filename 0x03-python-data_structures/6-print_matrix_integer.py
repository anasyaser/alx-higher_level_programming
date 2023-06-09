#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    for row in matrix:
        for num in row[:-1]:
            print("{}".format(num), end=' ')
        print("{}".format(row[-1]))
