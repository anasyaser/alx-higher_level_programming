#!/usr/bin/python3
"""Check if obj is instance of inherited class"""


def inherits_from(obj, a_class):
    """
    Check if obect class is inherited from class

    Args:
        obj: boject
        a_class: class

    Return:
        True if obj class is inherited from a_class else False
    """
    return isinstance(obj, a_class) and type(obj).__name__ != a_class.__name__

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
