#!/usr/bin/python
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_1(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_2(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_noitem(self):
        self.assertEqual(max_integer([]), None)

    def test_oneitem(self):
        self.assertEqual(max_integer([1]), 1)

if __name__ == "__main__":
    unittest.main()
