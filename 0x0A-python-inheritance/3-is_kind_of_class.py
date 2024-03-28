#!/usr/bin/python3
"""
A function that returns whether the object is an instance of the class that
inherited from the specific class or not.
"""


def is_kind_of_class(obj, a_class):
    """ Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class;
    otherwise, returns False."""
    return isinstance(obj, a_class)
