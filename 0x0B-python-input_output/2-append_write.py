#!/usr/bin/python3
"""Defines appending file function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)
    Args:
        filename (str): The name of the file.
        text (str): The string to append.
    Returns:
        The number of characters apended"""
    with open(filename, "a") as f:
        return f.write(text)
