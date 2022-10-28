#!/usr/bin/python3
"""Defines Json string to object function"""

import json


def from_json_string(my_str):
    """Function to return an object represented by a JSON string """
    return json.loads(my_str)
