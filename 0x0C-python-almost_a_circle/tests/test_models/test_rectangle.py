from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rec1 = Rectangle(3, 5)
        self.rec2 = Rectangle(3, 6, 3, 8, 101)

    def test_attributes(self):
        self.assertEqual(self.rec1.width, 3)
        self.assertEqual(self.rec2.height, 6)

        self.assertEqual(self.rec1.x, 0)
        self.assertEqual(self.rec1.y, 0)
        self.assertEqual(self.rec2.x, 3)
        self.assertEqual(self.rec2.y, 8)

        self.assertEqual(self.rec1.id, 1)
        self.assertEqual(self.rec2.id, 101)

        with self.assertRaises(TypeError):
            self.rec1.width = 1.2
            self.rec1.height = 1.2
            self.rec1.width = "a"
            self.rec1.height = True
            self.rec1.x = 1.5
            self.rec1.y = 8.2

        with self.assertRaises(ValueError):
            self.rec1.width = 0
            self.rec1.height = -1
            self.rec1.x = -2
            self.rec1.y = -1.2

    def test_area(self):
        self.assertEqual(self.rec1.area(), 15)
        self.assertEqual(self.rec2.area(), 18)

    def test_rectangleRepresentation(self):
        rep1 = "[Rectangle] (1) 0/0 - 3/5"
        rep2 = "[Rectangle] (101) 3/8 - 3/6"

        self.assertEqual(str(self.rec1), rep1)
        self.assertEqual(str(self.rec2), rep2)

    def test_updatePositional(self):
        # add test case which not provide a;; args
        self.rec1.update(200, 7, 3, 1, 2)
        msg = "[Rectangle] (200) 1/2 - 7/3"
        self.assertEqual(str(self.rec1), msg)

        self.rec1.update(100, 8, 9, 2)
        msg = "[Rectangle] (100) 2/2 - 8/9"
        self.assertEqual(str(self.rec1), msg)

        self.rec1.update(100, 8, 3)
        msg = "[Rectangle] (100) 2/2 - 8/3"
        self.assertEqual(str(self.rec1), msg)

        self.rec1.update(100, 10)
        msg = "[Rectangle] (100) 2/2 - 10/3"
        self.assertEqual(str(self.rec1), msg)

        self.rec1.update(105)
        msg = "[Rectangle] (105) 2/2 - 10/3"
        self.assertEqual(str(self.rec1), msg)

        with self.assertRaises(TypeError):
            self.rec2.update(112, 1, 2.3, 1, 2)

        with self.assertRaises(ValueError):
            self.rec2.update(112, 1, 3, -1, 2)

    def ttest_updateKeyword(self):
        self.rec1.update(200, 7, 3, 1, 2)
        msg = "[Rectangle] (200) 1/2 - 7/3"
        self.assertEqual(str(self.rec1), msg)

        self.rec1.update(width=8, x=2, id=100, height=9)
        msg = "[Rectangle] (100) 2/2 - 8/9"
        self.assertEqual(str(self.rec1), msg)

        self.rec1.update(x=8, y=3, id=110)
        msg = "[Rectangle] (110) 8/3 - 8/9"
        self.assertEqual(str(self.rec1), msg)

        self.rec1.update(width=10)
        msg = "[Rectangle] (100) 8/3 - 10/9"
        self.assertEqual(str(self.rec1), msg)

        self.rec1.update(id=105)
        msg = "[Rectangle] (105) 8/3 - 10/9"
        self.assertEqual(str(self.rec1), msg)

        with self.assertRaises(TypeError):
            self.rec2.update(width=1.2)
            self.rec2.update(height=1.2)

        with self.assertRaises(ValueError):
            self.rec2.update(x=-2)
            self.rec2.update(y=-2)
            self.rec2.update(width=-2)
