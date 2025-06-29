#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize Square with size (validated and used for both width and height).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
