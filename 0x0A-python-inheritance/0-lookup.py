#!/usr/bin/python3
"""
A function to lookup object attributes.
"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object."""
    return dir(obj)
