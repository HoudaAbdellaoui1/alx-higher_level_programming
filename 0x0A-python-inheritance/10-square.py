#!/usr/bin/python3
""" Square module """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class with private size attribute & area method"""
    def __init__(self, size):
        """Instantiates a Square object with a given size."""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Computes and returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of the square
        in the format [Rectangle] <size>/<size>."""
        return f"[Rectangle] {self.__size}/{self.__size}"
