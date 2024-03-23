#!/usr/bin/python3
import json
"""From JSON to object """


def from_json_string(my_str):
    """return an object (Python data structure) 
    represented by a JSON string.

        Args:
            my_str (string): string to be converted.
        Returns:
            Object.
    """
    return (json.loads(my_str))