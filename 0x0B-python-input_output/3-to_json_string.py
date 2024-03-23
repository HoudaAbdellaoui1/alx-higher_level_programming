#!/usr/bin/python3
import json
"""JSON Representation"""


def to_json_string(my_obj):
    """return JSON representation of an object.

        Args:
            my_obj (object): object to be converted.
        Returns:
            JSON Object.
    """
    return (json.dumps(my_obj))
