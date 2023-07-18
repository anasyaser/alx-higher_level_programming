#!/usr/bin/python3
"""
Module: models

Base class for all other classes in project
"""
import json


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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaryies):
        """json string representation of dictionaries"""
        if list_dictionaryies:
            return json.dumps(list_dictionaryies)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """save list of class instance attributes to json file"""
        file_name = cls.__name__ + ".json"

        with open(file_name, "w") as f:
            lst_dicts = []
            if list_objs:
                lst_dicts = [inst.to_dictionary() for inst in list_objs]
            f.write(Base.to_json_string(lst_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Create list of json string representation"""
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        if dictionary:
            new_instance = cls(1, 1)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        lst_objs = []
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r") as f:
                lst_dicts = Base.from_json_string(f.read())
                for dicts in lst_dicts:
                    lst_objs.append(cls.create(**dicts))
        except FileNotFoundError:
            return lst_objs
        return lst_objs
