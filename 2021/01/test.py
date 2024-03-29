#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code

class TestDay01(unittest.TestCase):
    # Part 01
    def test_example01(self):
        measures = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        expected = 7

        result = code.part01(measures)
        self.assertEqual(result, expected)

    # Part 02
    def test_example02(self):
        measures = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        expected = 5

        result = code.part02(measures)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
