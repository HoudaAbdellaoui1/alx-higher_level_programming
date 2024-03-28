#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_id_increment(self):
        # Test that each instance gets a unique ID
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_id_assignment(self):
        # Test that the ID is assigned when provided
        base_with_id = Base(5)
        self.assertEqual(base_with_id.id, 5)

    def test_id_default_value(self):
        # Test that the default value of ID is incremental
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_id_negative_value(self):
        self.assertEqual(-1, Base(-1).id)

    def test_id_string_value(self):
        self.assertEqual("hello", Base("hello").id)


if __name__ == '__main__':
    unittest.main()
