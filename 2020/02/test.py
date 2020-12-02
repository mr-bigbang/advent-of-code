#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code

class TestDay02(unittest.TestCase):
    # Part 01
    def test_example01(self):
        passwords = ["1-3 a: abcde",
                     "1-3 b: cdefg",
                     "2-9 c: ccccccccc"]
        expected = 2

        result = code.part01(passwords)
        self.assertEqual(result, expected)

    # Part 02
    def test_example02(self):
        passwords = ["1-3 a: abcde",
                     "1-3 b: cdefg",
                     "2-9 c: ccccccccc"]
        expected = 1

        result = code.part02(passwords)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
