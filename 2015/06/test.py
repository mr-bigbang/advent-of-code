#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code

class TestDay06(unittest.TestCase):
    # Part 01
    def test_example01(self):
        instructions = ["turn on 0,0 through 999,999"]
        expected = 1000000

        result = code.part01(instructions)
        self.assertEqual(result, expected)

    def test_example02(self):
        instructions = ["toggle 0,0 through 999,0"]
        expected = 1000

        result = code.part01(instructions)
        self.assertEqual(result, expected)

    def test_example03(self):
        instructions = ["turn off 499,499 through 500,500"]
        expected = 0

        result = code.part01(instructions)
        self.assertEqual(result, expected)

    # Part 02
    def test_example04(self):
        instructions = ["turn on 0,0 through 0,0"]
        expected = 1

        result = code.part02(instructions)
        self.assertEqual(result, expected)

    def test_example05(self):
        instructions = ["toggle 0,0 through 999,999"]
        expected = 2000000

        result = code.part02(instructions)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
