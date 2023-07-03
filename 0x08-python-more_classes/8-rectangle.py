#!/usr/bin/python3
"""
Create Rectangle wiht some features
"""


class Rectangle:
    """
    Create Rectangle with some features

    Args:
        widht: (int) width of rectangle
        height: (int) height of rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieving rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setup rectangle width
        Args:
            value: (int) rectangle width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieving rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        setup rectangle height
        Args:
            value: (int) rectangle height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate rectangle perimeter
        (Alert: if any dimension is zero return 0)
        """
        if self.area() == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        rec_str = ""
        if self.area() != 0:
            symbol_str = str(self.print_symbol)
            for i in range(self.height):
                rec_str += symbol_str * self.width + "\n"
        return rec_str[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
