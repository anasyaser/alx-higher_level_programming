#!/usr/bin/python3
"""
4-print_square

print square shape of symbole #
"""


def print_square(size):
    """
    print square shape of # symbole

    Args:
        size: (int -> must be larger than -1) size of square shape
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
    if size == 0:
        print()
