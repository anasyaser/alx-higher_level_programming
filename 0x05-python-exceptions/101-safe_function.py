#!/usr/bin/python3
import sys


def safe_function(func, *arg):
    try:
        return func(*arg)
    except Exception as ex:
        print("Exception: {}".format(ex.args[0]), file=sys.stderr)
