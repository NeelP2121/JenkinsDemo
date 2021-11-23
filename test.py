#!/usr/bin/python3
import unittest

from code import *

class Test(unittest.TestCase):
    def test_addition(self):
        data = [6, 24]
        expected = 30
        self.assertEqual(addition(data[0], data[1]), expected)

    def test_subtraction(self):
        data = [6, 24]
        expected = -18
        self.assertEqual(subtraction(data[0], data[1]), expected)

    def test_multiplication(self):
        data = [6, 24]
        expected = 144
        self.assertEqual(multiplication(data[0], data[1]), expected)

    def test_division(self):
        data = [24, 12]
        expected = 2
        self.assertAlmostEqual(division(data[0], data[1]), expected)

if __name__ == '__main__':
    unittest.main()
