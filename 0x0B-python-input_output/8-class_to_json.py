#!/usr/bin/python3
"""
Convert class to json object
"""
import json


def class_to_json(obj):
    """Convert calss attributes to python dictionary"""
    return vars(obj)
