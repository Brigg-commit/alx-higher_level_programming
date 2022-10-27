#!/usr/bin/python3
"""Define module read text reading"""


def read_file(filename=""):
    """Print the contents of a UTF-8 text file to stdout"""
    with open(filename, "r") as f:
        print(f.read(), end="")
