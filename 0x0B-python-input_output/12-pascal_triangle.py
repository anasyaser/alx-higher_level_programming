#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    lst = []
    for i in range(n - 1):
        lst_inner = []
        lst_inner.append(1)
        tmp = 0
        for i in range(len(lst)):
            lst[i], tmp = lst[i] + tmp, lst[i]

    return lst


pascal_triangle(5)
