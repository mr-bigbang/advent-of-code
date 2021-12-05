#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code


class TestDay05(unittest.TestCase):
    def setUp(self):
        self.data = tuple([
            "0, 9 -> 5, 9",
            "8, 0 -> 0, 8",
            "9, 4 -> 3, 4",
            "2, 2 -> 2, 1",
            "7, 0 -> 7, 4",
            "6, 4 -> 2, 0",
            "0, 9 -> 2, 9",
            "3, 4 -> 1, 4",
            "0, 0 -> 8, 8",
            "5, 5 -> 8, 2",
        ])

        with open("input.txt", "r") as f:
            self.input = f.readlines()

    # Part 01
    def test_example01(self):
        expected = 5

        result = code.part01(self.data)
        self.assertEqual(expected, result)

    def test_result01(self):
        expected = 7674

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
