#!/usr/bin/python3
"""Return max integer."""


def max_integer(list=[]):
    """Return max integer

    Args:
        list (array): The list to be analyzed.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 0
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
