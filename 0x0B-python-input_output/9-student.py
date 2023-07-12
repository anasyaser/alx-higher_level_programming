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

    def to_json(self):
        """Retrieve dictionary of class attributes to convert to json"""
        return vars(self)
