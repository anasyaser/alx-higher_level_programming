#!/usr/bin/python3
"""Check if obj is instance of class"""


def is_same_class(obj, a_class):
    """
    Check if obect is instance of class

    Args:
        obj: boject
        a_class: class

    Return:
        True if obj is instance of a_class else False
    """
    return isinstance(obj, a_class)
