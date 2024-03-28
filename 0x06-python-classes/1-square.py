#!/usr/bin/python3
"""Defines a square with size attribute """


class Square:
    """
    This class defines a square by encapsulating the size as a private instance attribute.

    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int): The size of the square. No type or value verification is performed.
        """
        self.__size = size
