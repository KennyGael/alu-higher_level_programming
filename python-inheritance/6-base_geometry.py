#!/usr/bin/python3
"""
This module defines a class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """
    BaseGeometry class intended to be extended later.
    """

    def area(self):
        """
        Raises an exception to indicate the method is not implemented.

        Raises:
            Exception: with message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")
