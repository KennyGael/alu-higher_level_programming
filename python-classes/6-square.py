#!/usr/bin/python3
"""Module that defines a class Square with position and print."""


class Square:
    """Represents a square with size, position, area, and print behavior."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using # characters with position offset."""
        if self.__size == 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
