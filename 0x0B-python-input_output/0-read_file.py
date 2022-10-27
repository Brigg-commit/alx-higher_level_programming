#!/usr/bin/python3
"""Define module read text reading"""


def read_file(filename=""):
    """Function to read a text file (UTF8) and prints it to stdout"""
    
    with open(filename, "r") as f
    print(f.read(), end="")

