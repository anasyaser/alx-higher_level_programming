#!/usr/bin/python3
"""
Rectangle Module

Create Geometry shape ()Rectangle)
"""


class Rectangle(BaseGeometry):
    """
    Create recatangle

    attributes:
        widht: rectangle width
        height: rectangle height
    """
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set recatgle width"""
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Get rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set recatangel Height"""
        self.integer_validator("width", value)
        self.__height = value
