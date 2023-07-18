from models.square import Square
import unittest


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.squr1 = Square(5)
        self.squr2 = Square(4, 3, 8, 101)

    def test_attributes(self):
        self.assertEqual(self.squr1.size, 3)

        self.assertEqual(self.squr1.x, 0)
        self.assertEqual(self.squr1.y, 0)
        self.assertEqual(self.squr2.x, 3)
        self.assertEqual(self.squr2.y, 8)

        self.assertEqual(self.squr1.id, 1)
        self.assertEqual(self.squr2.id, 101)

        with self.assertRaises(TypeError):
            self.squr1.size = 1.2
            self.squr1.size = "a"
            self.squr1.size = True
            self.squr1.x = 1.5
            self.squr1.y = 8.2

        with self.assertRaises(ValueError):
            self.squr1.size = 0
            self.squr1.size = -1
            self.squr1.x = -2
            self.squr1.y = -1.2

    def test_area(self):
        self.assertEqual(self.squr1.area(), 25)
        self.assertEqual(self.squr2.area(), 16)

    def test_rectangleRepresentation(self):
        rep1 = "[Square] (1) 0/0 - 5"
        rep2 = "[Square] (101) 3/8 - 4"

        self.assertEqual(str(self.squr1), rep1)
        self.assertEqual(str(self.squr2), rep2)

    def test_updatePositional(self):
        # add test case which not provide a;; args
        self.squr1.update(200, 7, 1, 2)
        msg = "[Square] (200) 1/2 - 7"
        self.assertEqual(str(self.squr1), msg)

        self.squr1.update(100, 8, 9, 2)
        msg = "[Square] (100) 2/2 - 8/9"
        self.assertEqual(str(self.squr1), msg)

        self.squr1.update(100, 8, 3)
        msg = "[Square] (100) 2/2 - 8/3"
        self.assertEqual(str(self.squr1), msg)

        self.squr1.update(100, 10)
        msg = "[Square] (100) 2/2 - 10/3"
        self.assertEqual(str(self.squr1), msg)

        self.squr1.update(105)
        msg = "[Square] (105) 2/2 - 10/3"
        self.assertEqual(str(self.squr1), msg)

        with self.assertRaises(TypeError):
            self.squr2.update(112, 1, 2.3, 1, 2)

        with self.assertRaises(ValueError):
            self.squr2.update(112, 1, 3, -1, 2)

    def ttest_updateKeyword(self):
        self.squr1.update(200, 7, 1, 2)
        msg = "[Square] (200) 1/2 - 7"
        self.assertEqual(str(self.squr1), msg)

        self.squr1.update(size=8, x=2, id=100)
        msg = "[Square] (100) 2/2 - 8"
        self.assertEqual(str(self.squr1), msg)

        self.squr1.update(x=8, y=3, id=110)
        msg = "[Square] (110) 8/3 - 8"
        self.assertEqual(str(self.squr1), msg)

        self.squr1.update(size=10)
        msg = "[Square] (100) 8/3 - 10"
        self.assertEqual(str(self.squr1), msg)

        self.squr1.update(id=105)
        msg = "[Square] (105) 8/3 - 10"
        self.assertEqual(str(self.squr1), msg)

        with self.assertRaises(TypeError):
            self.squr2.update(size=1.2)
            self.squr2.update(size=1.2)

        with self.assertRaises(ValueError):
            self.squr2.update(x=-2)
            self.squr2.update(y=-2)
            self.squr2.update(size=-2)
