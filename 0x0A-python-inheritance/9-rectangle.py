#!/usr/bin/python3
"""
Rectangle Module

Create Geometry shape ()Rectangle)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Create recatangle

    attributes:
        width: rectangle width
        height: rectangle height
    """
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate Rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
