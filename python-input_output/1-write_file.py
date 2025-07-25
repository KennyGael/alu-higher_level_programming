#!/usr/bin/python3
"""Module that writes text to a file and returns number of characters written"""


def write_file(filename="", text=""):
    """Write *text* to *filename* and return number of characters written"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
