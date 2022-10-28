#!/usr/bin/python3
"""Defines JSON string function."""

import json


def to_json_string(my_obj):
    """Function that return JSON representation of an object """
    return json.dumps(my_obj)
