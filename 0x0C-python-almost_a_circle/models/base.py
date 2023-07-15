#!/usr/bin/python3
"""
Module: models

Base class for all other classes in project
"""


class Base:
    """
    Base class for all other classes in project

    attributes:
        id: instanse id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
