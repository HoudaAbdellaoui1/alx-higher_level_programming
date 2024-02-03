#!/usr/bin/python3
""" Rectangle module """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from base geometry"""
    def __init__(self, width, height):
        """Instantiates a Rectangle object with width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
