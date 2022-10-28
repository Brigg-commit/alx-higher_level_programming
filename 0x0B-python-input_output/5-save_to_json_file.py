#!/usr/bin/python3
"""Writes an object to a file function"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using JASON.
    Args:
    Returns:"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
