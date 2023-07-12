#!/usr/bin/python3
"""
Convert class to json object
"""


def class_to_json(obj):
    """Convert calss attributes to python dictionary"""
    return vars(obj)
