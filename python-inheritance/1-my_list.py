#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list
and includes a method to print the list in sorted order.
"""


class MyList(list):
    """
    MyList class that extends the built-in list with a print_sorted method.
    """

    def print_sorted(self):
        """
        Returns the list in ascending sorted order.

        Example:
        >>> my_list = MyList()
        >>> my_list.extend([3, 1, 4])
        >>> my_list.print_sorted()
        [1, 3, 4]
        """
        return sorted(self)
