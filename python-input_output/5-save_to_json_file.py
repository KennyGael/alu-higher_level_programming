#!/usr/bin/python3
"""Save object to file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Write object to text file using JSON representation"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
