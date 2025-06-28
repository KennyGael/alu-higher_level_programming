#!/usr/bin/python3
"""
This module defines a custom list class that inherits from list and
adds a method to print the list sorted without modifying the original list.
"""

class MyList(list):
    """
    A subclass of list with an additional method to print the list sorted.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order without changing the original list.
        """
        print(sorted(self))
