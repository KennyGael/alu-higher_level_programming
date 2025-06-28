#!/usr/bin/python3
"""1-my_list module: defines a class MyList that inherits from list"""

class MyList(list):
    """Custom list class that extends built-in list"""

    def print_sorted(self):
        """Prints the list in ascending sorted order"""
        print(sorted(self))
