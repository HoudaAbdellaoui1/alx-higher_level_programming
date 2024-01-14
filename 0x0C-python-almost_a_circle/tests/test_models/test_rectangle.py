#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Unittests for testing instantiation of the rectangle class."""

    def test_constructor(self):
        # Test the constructor with valid values
        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 1)

    def test_width_negative_value(self):
        # Test that setting a negative width raises a ValueError
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-5, 10, 2, 3, 1)

    def test_height_string_value(self):
        # Test that setting a string height raises a TypeError
        with self.assertRaises(TypeError):
            rectangle = Rectangle(5, "10", 2, 3, 1)

    def test_x_setter(self):
        # Test the x setter method
        rectangle = Rectangle(5, 10, 2, 3, 1)
        rectangle.x = 7
        self.assertEqual(rectangle.x, 7)

    def test_y_default_value(self):
        # Test that y has a default value of 0
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.y, 0)

    def test_width_zero_value(self):
        # Test that setting width to 0 raises a ValueError
        with self.assertRaises(ValueError):
            rectangle = Rectangle(0, 10, 2, 3, 1)

    def test_height_zero_value(self):
        # Test that setting height to 0 raises a ValueError
        with self.assertRaises(ValueError):
            rectangle = Rectangle(5, 0, 2, 3, 1)

    def test_x_negative_value(self):
        # Test that setting a negative x raises a ValueError
        with self.assertRaises(ValueError):
            rectangle = Rectangle(5, 10, -2, 3, 1)

    def test_y_negative_value(self):
        # Test that setting a negative y raises a ValueError
        with self.assertRaises(ValueError):
            rectangle = Rectangle(5, 10, 2, -3, 1)

if __name__ == '__main__':
    unittest.main()
