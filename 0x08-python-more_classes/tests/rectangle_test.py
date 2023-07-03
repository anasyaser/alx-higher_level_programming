#!/usr/bin/python3
"""
Tests for rectangle module
"""
import unittest
Rectangle = __import__("0-rectangle").Rectangle

class RectangleTest(unittest.TestCase):

    def setUp(self):
        """Setting Recatngle to Test"""
        print("setUp")
        self.rectangle1 = Rectangle()

    def test_widht_height(self):
        """
        Test for setting and retrieving recatangle width and height
        """
        print("Width and Height Test")
        with self.assertRaises(TypeError):
            self.rectangle1.width = "cc"
            self.rectangle1.height = "ss"

        with self.assertRaises(ValueError):
            self.rectangle1.width = -1
            self.rectangle1.height = -1

        self.assertEqual(self.rectangle1.width, 0)
        self.assertEqual(self.rectangle1.height, 0)

        self.rectangle1.width = 3
        self.rectangle1.height = 5
        self.assertEqual(self.rectangle1.width, 3)
        self.assertEqual(self.rectangle1.height, 5)
