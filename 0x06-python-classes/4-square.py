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
        self.size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the Square object.

        This method provides a human-readable string that represents the
        Square object. It is useful for debugging and informative purposes.
        """
        return f"Square with size: {self.__size}"

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
        - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Parameters:
        - value (int): The new size of the square.
          Raises:
          - TypeError: If value is not an integer.
          - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
