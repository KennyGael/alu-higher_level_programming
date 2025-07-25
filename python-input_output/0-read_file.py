#!/usr/bin/python3
"""Module for reading and printing a text file (UTF8)"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
