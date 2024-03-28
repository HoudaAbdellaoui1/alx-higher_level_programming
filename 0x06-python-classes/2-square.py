#!/usr/bin/python3
"""Defines a square with size attribute """


class Square:
    """
    This class defines a square by encapsulating the size as a private instance attribute.

    The square is characterized by having all sides of equal length.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class with an optional size parameter.

        Parameters:
        - size (int, optional): The size of the square. Default is 0.
          Raises:
          - TypeError: If size is not an integer.
          - ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
