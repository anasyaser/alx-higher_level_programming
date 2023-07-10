#!/usr/bin/python3
"""Check if obj is instance of inherited class"""


def inherits_from(obj, a_class):
    """
    Check if obect is inherited from class

    Args:
        obj: boject
        a_class: class

    Return:
        True if obj is inherited from a_class else False
    """
    return isinstance(obj, a_class)
