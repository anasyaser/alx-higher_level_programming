#!/usr/bin/python3
"""
Read File and print it to stdout
"""


def read_file(file_name=""):
    """Read file and print its content"""
    with open(file_name, "r") as f:
        print(f.read())
