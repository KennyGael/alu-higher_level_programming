#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle
and overrides __str__ to return a Square-specific description.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize Square with size.

        Validates size and uses it for both width and height.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
