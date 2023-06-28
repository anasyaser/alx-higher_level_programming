#!/usr/bin/python3
"Creating Geometry shape"


class Square:
    """
    Creating Geometry shape: Square

    Args:
        size:(int) square size
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
