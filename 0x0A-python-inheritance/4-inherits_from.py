#!/usr/bin/python3
"""
A function that returns whether the object is an instance of the class that inherited (directly or indirectly)
from the specific class or not.
"""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class."""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
