#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code

class TestDay02(unittest.TestCase):
    # Part 01
    def test_example01(self):
        package = ["2x3x4", ]
        expected = 58

        result = code.part01(package)
        self.assertEqual(result, expected)

    def test_example02(self):
        package = ["1x1x10", ]
        expected = 43

        result = code.part01(package)
        self.assertEqual(result, expected)

    # Part 02

if __name__ == '__main__':
    unittest.main()
