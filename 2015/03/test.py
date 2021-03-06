#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code

class TestDay03(unittest.TestCase):
    # Part 01
    def test_example01(self):
        directions = ">"
        expected = 2

        result = code.part01(directions)
        self.assertEqual(result, expected)

    def test_example02(self):
        directions = "^>v<"
        expected = 4

        result = code.part01(directions)
        self.assertEqual(result, expected)

    def test_example03(self):
        directions = "^v^v^v^v^v"
        expected = 2

        result = code.part01(directions)
        self.assertEqual(result, expected)

    # Part 02
    def test_example04(self):
        directions = "^v"
        expected = 3

        result = code.part02(directions)
        self.assertEqual(result, expected)

    def test_example05(self):
        directions = "^>v<"
        expected = 3

        result = code.part02(directions)
        self.assertEqual(result, expected)

    def test_example06(self):
        directions = "^v^v^v^v^v"
        expected = 11

        result = code.part02(directions)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
