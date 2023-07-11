#!/usr/bin/python3
"""
Write to File
"""


def write_file(file_name="", text=""):
    """Write to file and return how many chars have been written"""
    with open(file_name, "w", encoding='utf-8') as f:
        return f.write(text)
