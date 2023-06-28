#!/usr/bin/python3
"Creating Geometry shape"


class Square:
    """
    Creating Geometry shape: Square

    Args:
        size:(int) square size
    """
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        """Getter attribute: size"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter attribute: size

        Args:
            value:(int) size value
        """
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        self.__size = value
