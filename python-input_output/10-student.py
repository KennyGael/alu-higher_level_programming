#!/usr/bin/python3
"""Student class with attribute filtering"""


class Student:
    """Define a student with optional JSON filtering"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dict of Student instance, optionally filtered"""
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
        return self.__dict__
