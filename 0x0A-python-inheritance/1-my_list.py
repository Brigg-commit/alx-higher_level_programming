#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(List):
    """A subclass of list"""
    def print_sorted(self):
        """Prints the list in asorted ascending order"""
        print(sorted(self))
