#!/usr/bin/python3
"""This module defines a class MyList that inherits from list."""


class MyList(list):
    """A subclass of list with a method to print sorted elements."""

    def print_sorted(self):
        """Prints the list in ascending order.

        This method does not modify the original list.
        """
        print(sorted(self))
