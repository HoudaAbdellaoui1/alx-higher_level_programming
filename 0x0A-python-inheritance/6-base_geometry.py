#!/usr/bin/python3
""" Base Geometry module with area method """


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")
