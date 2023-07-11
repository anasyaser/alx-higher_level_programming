#!/usr/bin/python3
"""
Append to File
"""


def append_write(file_name="", text=""):
    """append to file and return how many chars have been written"""
    with open(file_name, "a", encoding='utf-8') as f:
        return f.write(text)
