#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code


class TestDay06(unittest.TestCase):
    def setUp(self):
        self.data = (3, 4, 3, 1, 2)

        with open("input.txt", "r") as f:
            self.input = tuple(map(int, f.read().split(',')))

    # Part 01
    def test_example01(self):
        expected = 5934

        result = code.part01(self.data)
        self.assertEqual(expected, result)

    def test_result01(self):
        expected = 390011

        result = code.part01(self.input)
        self.assertEqual(expected, result)

    # Part 02
    # def test_example02(self):
    #     expected = None
    #
    #     result = code.part02(self.data)
    #     self.assertEqual(expected, result)
    #
    # def test_result02(self):
    #     expected = None
    #
    #     result = code.part02(self.input)
    #     self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
