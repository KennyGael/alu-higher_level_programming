#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance of
a specified class or a class that inherits from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or a subclass of a_class,
    otherwise False.

    Args:
        obj: any object
        a_class: the class to check against

    Returns:
        True if obj is instance or inherits from a_class, else False
    """
    return isinstance(obj, a_class)
