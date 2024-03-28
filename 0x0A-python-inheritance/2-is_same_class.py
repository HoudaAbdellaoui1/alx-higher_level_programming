#!/usr/bin/python3
"""
A function that returns whether the object is an instance of the specified
class or not.
"""


def is_same_class(obj, a_class):
    """ Returns True if the object is exactly an instance of the
    specified class; otherwise, returns False."""
    return type(obj) is a_class
