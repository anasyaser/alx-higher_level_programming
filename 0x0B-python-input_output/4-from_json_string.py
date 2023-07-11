#!/usr/bin/python3
"""
Convert json object to python data structure
"""
import json


def from_json_string(my_obj):
    """Convert json object to Python object"""
    return json.loads(my_obj)
