#!/usr/bin/python3
"""Class to dictionary representation for JSON serialization"""


def class_to_json(obj):
    """Return dict description for JSON serialization"""
    return obj.__dict__
