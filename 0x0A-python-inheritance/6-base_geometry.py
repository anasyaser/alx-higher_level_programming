#!/usr/bin/python3
"""Geometry Module"""


class BaseGeometry:
    """Base class for Geometry shaps"""
    def area(self):
        """Calculate geometry area"""
        raise Exception("area() is not implemented")
