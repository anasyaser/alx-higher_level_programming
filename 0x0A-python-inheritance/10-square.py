#!/usr/bin/python3
"""
Square Module

Create Geometry shape ()Square)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Create square

    attributes:
        size: square size
    """
    def __init__(self, size):
        super().__init__(size, size)
