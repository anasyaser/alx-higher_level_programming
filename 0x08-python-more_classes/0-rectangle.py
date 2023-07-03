#!/usr/bin/python3
"""
Create Rectangle wiht some features
"""


class Rectangle:
    """
    Create Rectangle with some features

    Args:
        widht: (int) width of rectangle
        height: (int) height of rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieving rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setup rectangle width
        Args:
            value: (int) rectangle width
        """
        if type(value) != int:
            raise TypeError("widht must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieving rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        setup rectangle height
        Args:
            value: (int) rectangle height
        """
        if type(value) != int:
            raise TypeError("widht must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
