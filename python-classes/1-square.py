#!/usr/bin/python3
"""Module that defines a class Square with a private size attribute."""


class Square:
    """Represents a square with a private size."""

    def __init__(self, size):
        """Initializes the square with a given size."""
        self.__size = size
