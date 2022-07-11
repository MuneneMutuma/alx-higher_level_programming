import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestCases(unittest.TestCase):
    def test_base1(self):
        base = Base()
        self.assertEqual(base.id, 1)
        base1 = Base(13)
        self.assertEqual(base1.id, 13)
        base2 = Base()
        self.assertEqual(base2.id, 2)

    def test_rectangle2(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 3)
        r2 = Rectangle(2, 4, 9, 9, 7)
        self.assertEqual(r2.id, 7)
        r3 = Rectangle(1, 1, 0, 0)
        self.assertEqual(r3.id, 4)

    def test_rectangle_setters_and_getters(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, "2")
        e1 = e.exception
        self.assertEqual(type(e1), TypeError)

        with self.assertRaises(ValueError) as e:
            Rectangle(-1, 2)
        e2 = e.exception
        self.assertEqual(type(e2), ValueError)

        with self.assertRaises(TypeError) as e:
            Rectangle("2", 3)
        e2 = e.exception
        self.assertEqual(type(e2), TypeError)

    def test_rectangle_area(self):
        r4 = Rectangle(3, 2)
        self.assertEqual(r4.area(), 6)

        r5 = Rectangle(9, 7)
        self.assertEqual(r5.area(), 63)

        r6 = Rectangle(7, 13, 0, 1, 13)
        self.assertEqual(r6.area(), 91)


if __name__ == "__main__":
    unittest.main()
