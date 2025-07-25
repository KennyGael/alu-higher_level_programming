#!/usr/bin/python3
"""Student class with reload from JSON"""


class Student:
    """Define a student with JSON serialization and reloading"""

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

    def reload_from_json(self, json):
        """Replace attributes using dictionary values"""
        for key, value in json.items():
            setattr(self, key, value)
