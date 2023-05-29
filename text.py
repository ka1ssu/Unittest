import unittest
from main import test1

class TestSite(unittest.TestCase):

    def test_string(self):
        self.assertEqual(test1("1"), 1)
        self.assertEqual(test1("-2"), "That's wrong")
        self.assertEqual(test1(" "), "That's wrong")
        self.assertEqual(test1("#"), "That's wrong")
        self.assertEqual(test1("mathematic"), "That's wrong")
        self.assertEqual(test1(1.2), "That's wrong")