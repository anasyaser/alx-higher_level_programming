#!/usr/bin/python3
"""Creat magic class"""


class MagicClass:
    """
    Create Magic class

    Attributes:
        radius: circle radius
    """

    def __init__(self, radius=0):
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate area of circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate circumference of circle"""
        return 2 * math.pi * self.__radius
