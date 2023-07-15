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

        self.assertEqual(self.rec1.__str__(), rep1)
        self.assertEqual(self.rec2.__str__(), rep2)

    def test_update(self):
        # add test case which not provide a;; args
        self.rec1.update(200, 7, 3, 1, 2)
        self.assertEqual(self.rec1.width, 7)
        self.assertEqual(self.rec1.height, 3)
        self.assertEqual(self.rec1.x, 1)
        self.assertEqual(self.rec1.y, 2)
        self.assertEqual(self.rec1.id, 200)

        with self.assertRaises(TypeError):
            self.rec2.update(112, 1,2, 3, 1, 2)

        with self.assertRaises(ValueError):
            self.rec2.update(112, 1, 3, -1, 2)
