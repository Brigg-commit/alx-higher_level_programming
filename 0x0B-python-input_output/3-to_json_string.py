#!/usr/bin/python3
"""Defines JSON string function."""

import jason


def to_json_string(my_obj):
    """Function that return JASON representation of an object """
    return jason.dumps(my_obj)
