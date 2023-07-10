#!/usr/bin/python3
"""
Create my own List
"""


class MyList(list):
    """
    Create my own list methods
    """
    def print_sorted(self):
        """print sorted list without modify original list"""
        print(sorted(self))
