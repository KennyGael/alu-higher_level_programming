#!/usr/bin/python3
"""
This module defines a single function that checks whether an object is exactly
an instance of a specific class, without considering inheritance.
"""

def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
