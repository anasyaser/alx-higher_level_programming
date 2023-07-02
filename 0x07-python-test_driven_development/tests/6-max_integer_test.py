#!usr/bin/python3
"""
6-max_integer_test

Test module for max_integer function
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def max_integer_test(self):
        lst1 = [1, 2, 3, 4]
        lst2 = [-1, 2, 3]

        self.assertIsNone(max_integer)
        self.assertEquale(max_integer(lst1), 4)
        self.assertEquale(max_integer(lst2), 3)
