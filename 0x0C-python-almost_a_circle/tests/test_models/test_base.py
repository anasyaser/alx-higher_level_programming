from models import base
import unittest


class TestBase(unittest.TestCase):

    def setUp(self):
        self.base1 = base.Base()
        self.base2 = base.Base(100)

    def test_attributes(self):
        self.assertIsNotNone(self.base1.id)
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 100)
        with self.assertRaises(AttributeError):
            self.base1.nb_objects
            self.base1.__nb_objects
