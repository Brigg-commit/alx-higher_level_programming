#!/usr/bin/python3
"""Defines a file writing function"""


def write_file(filename="", text=""):
    """ Write a string to a text file and returns the number of characters."""
    with open(filename, "w") as f:
        return f.write(text)
