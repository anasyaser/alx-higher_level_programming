#!/usr/bin/python3
"""
0-add_integer

Add two integer numbers
"""


def add_integer(a, b=98):
    """
    Add two integers

    Args:
        a: (int) first integer
        b: (int) second integer (default value = 98)

    Return:
        (int) summtion of two integers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
