#!/usr/bin/python3
"""
This module contains a function that returns the list
of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of attributes and methods of the given object.
    """
    return dir(obj)
