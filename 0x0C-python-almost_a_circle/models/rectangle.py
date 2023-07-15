#!/usr/bin/python3
"""
Module: models

Create Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Create Rectangle

    Attributes:
        width: rectangle width
        height: rectangel height
        x: x coordinate
        y: y coordinate
        id: shape instance id
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x offset getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x offset setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value


    @property
    def y(self):
        """y offset getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y offset setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Get recatangle area"""
        return self.width * self.height

    def display(self):
        """reprsent rectangle as # symbole"""
        pass

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args):
        """update rectangle attributes"""
        attrs = [self.id, self.width, self.height, self]
        for arg in enumerate(args):
            pass
