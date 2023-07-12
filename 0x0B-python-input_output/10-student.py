#!/usr/bin/python3
"""
Create student class and json method
"""


class Student:
    """
    Student class

    Args:
        first_name: student first name
        last_name: student last name
        age: student age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary of class attributes to convert to json"""
        all_attrs = vars(self)
        dict_attrs = {}
        if attrs:
            for attr in attrs:
                if attr in all_attrs:
                    dict_attrs[attr] = all_attrs[attr]
            return dict_attrs
        else:
            return all_attrs
