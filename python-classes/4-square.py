#!/usr/bin/python3
"""Module that defines a class Square with size getter and setter."""


class Square:
    """Represents a square with validated private size."""

    def __init__(self, size=0):
        """Initializes the square with optional validated size."""
        self.size = size

    @property
    def size(self):
        """Retrieves the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
