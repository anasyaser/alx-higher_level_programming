#!/usr/bin/python3
"""
Module: models

Create square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Create Rectangle

    Attributes:
        size: square size
        x: x coordinate
        y: y coordinate
        id: shape instance id
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = self.width
        self.__size = self.width

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
        """update rectangle attributes"""
        if args:
            try:
                super().__init__(self.width, self.height, id=args[0])
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key in kwargs.keys():
                value = kwargs[key]
                if key == "id":
                    super().__init__(self.width, self.height, id=value)
                    print("self.id", self.id)
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """get class attributes as dictionary"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
