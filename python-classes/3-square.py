#!/usr/bin/python3
"""Module that defines a class Square with area method."""


class Square:
    """Represents a square with validated private size."""

    def __init__(self, size=0):
        """Initializes the square with optional validated size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
