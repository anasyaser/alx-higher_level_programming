#!/usr/bin/python3
"""
Convert python data structure to json object and save it to file
"""
import json


def save_to_json_string(my_obj, file_name):
    """Convert Python object to json and save it to file"""
    with open(file_name, "w") as f:
        return json.dump(my_obj, f)
