#!/usr/bin/python3
"""Geometry Module"""


class BaseGeometry:
    """Base class for Geometry shaps"""

    def area(self):
        """Calculate geometry area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if value is valid integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        else:
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
