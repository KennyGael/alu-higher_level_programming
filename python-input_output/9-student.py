#!/usr/bin/python3
"""Student class definition"""


class Student:
    """Define a student with basic attributes"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dict representation of the Student instance"""
        return self.__dict__
