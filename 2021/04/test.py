#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code


class TestDay04(unittest.TestCase):
    def setUp(self):
        self.data = tuple([
            "7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1",
            "22 13 17 11  0\n8  2 23  4 24\n21  9 14 16  7\n6 10  3 18  5\n1 12 20 15 19",
            "3 15  0  2 22\n9 18 13 17  5\n19  8  7 25 23\n20 11 10 24  4\n14 21 16 12  6",
            "14 21 17 24  4\n10 16 15  9 19\n18  8 23 26 20\n22 11 13  6  5\n2  0 12  3  7",
        ])

        with open("input.txt", "r") as f:
            self.input = tuple(f.read().split('\n\n'))

    # Part 01
    def test_example01(self):
        expected = 4512

        result = code.part01(self.data)
        self.assertEqual(expected, result)

    def test_result01(self):
        expected = 39902

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
