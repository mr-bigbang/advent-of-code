#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code

class TestDay03(unittest.TestCase):
    def setUp(self):
        self.geology = ["..##.......",
                        "#...#...#..",
                        ".#....#..#.",
                        "..#.#...#.#",
                        ".#...##..#.",
                        "..#.##.....",
                        ".#.#.#....#",
                        ".#........#",
                        "#.##...#...",
                        "#...##....#",
                        ".#..#...#.#"]

    # Part 01
    def test_example01(self):
        expected = 7

        result = code.part01(self.geology)
        self.assertEqual(result, expected)

    # Part 02
    def test_example02(self):
        slope = (1, 1)
        expected = 2

        result = code.get_trees(self.geology, slope)
        self.assertEqual(result, expected)

    def test_example03(self):
        slope = (3, 1)
        expected = 7

        result = code.get_trees(self.geology, slope)
        self.assertEqual(result, expected)

    def test_example04(self):
        slope = (5, 1)
        expected = 3

        result = code.get_trees(self.geology, slope)
        self.assertEqual(result, expected)

    def test_example05(self):
        slope = (7, 1)
        expected = 4

        result = code.get_trees(self.geology, slope)
        self.assertEqual(result, expected)

    def test_example06(self):
        slope = (1, 2)
        expected = 2

        result = code.get_trees(self.geology, slope)
        self.assertEqual(result, expected)

    def test_example07(self):
        expected = 336

        result = code.part02(self.geology)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
