#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code


class TestDay07(unittest.TestCase):
    def setUp(self):
        self.data = (16, 1, 2, 0, 4, 2, 7, 1, 2, 14)

        with open("input.txt", "r") as f:
            self.input = tuple(map(int, f.read().split(',')))

    # Part 01
    def test_example01(self):
        expected = 37

        result = code.part01(self.data)
        self.assertEqual(expected, result)

    def test_result01(self):
        expected = 355592

        result = code.part01(self.input)
        self.assertEqual(expected, result)

    # Part 02
    def test_example02(self):
        expected = 168

        result = code.part02(self.data)
        self.assertEqual(expected, result)

    def test_result02(self):
        expected = 101618069

        result = code.part02(self.input)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
