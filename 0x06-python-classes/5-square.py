#!/usr/bin/python3
"Creating Geometry shape"


class Square:
    """
    Creating Geometry shape: Square

    Args:
        size:(int) square size
    """
    def __init__(self, size=0):
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
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate square area

        Return:
            (int) square area
        """

        return self.size * self.size

    def my_print(self):
        """
        Reperesent sqaure area as (#) char
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
