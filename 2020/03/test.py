#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code

class TestDay03(unittest.TestCase):
    # Part 01
    def test_example01(self):
        geology = ["..##.......",
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
        expected = 7

        result = code.part01(geology)
        self.assertEqual(result, expected)

    # Part 02
    pass

if __name__ == '__main__':
    unittest.main()
