#!/usr/bin/python3
"""Creating object from a jason file function."""


import json


def load_from_json_file(filename):
    """Represents function that creates an object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
