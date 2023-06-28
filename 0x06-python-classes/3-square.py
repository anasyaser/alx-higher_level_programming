#!/usr/bin/python3
"Creating Geometry shape"


class Square:
    """
    Creating Geometry shape: Square

    Args:
        size:(int) square size
    """
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.size = size

    def area(self):
        """
        Calculate square area

        Return:
            (int) square area
        """

        return self.size * self.size
