#!/usr/bin/python3
"""
Convert json object to python data structure
"""
import json


def load_from_json_file(file_name):
    """Convert json object to Python object"""
    with open(file_name, "r") as f:
        return json.load(f)
