import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_str(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_update(self):
        square = Square(5, 2, 3, 1)
        square.update(2, 10, 4, 2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 2)

    def test_update_kwargs(self):
        square = Square(5, 2, 3, 1)
        square.update(id=2, size=10, x=4, y=2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 2)

    def test_area(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.area(), 25)

if __name__ == '__main__':
    unittest.main()
