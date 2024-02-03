#!/usr/bin/python3
""" Base Geometry module with area method """


class BaseGeometry:
    """A class with public attribute area and integer validator"""
    def area(self):
        """raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates the value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
