#!/usr/bin/python3
"Creating Geometry shape"


class Square:
    """
    Creating Geometry shape: Square

    Args:
        size:(int) square size
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter for position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Attribute Setter: position

        Args:
            value: (tuple) of two positive integers
        """
        if isinstance(value, tuple) and (len(value) == 2) and\
           isinstance(value[0], int) and isinstance(value[1], int) and\
           value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Calculate square area

        Return:
            (int) square area
        """

        return self.size * self.size

    def __str__(self):
        """
        Reperesent sqaure area as (#) char
        """
        string = ""
        if self.size == 0:
            string += "\n"
        else:
            string += "\n" * self.position[1]
            for i in range(self.size):
                string += " " * self.position[0]
                string += "#" * self.size + "\n"
        return string[:-1]
