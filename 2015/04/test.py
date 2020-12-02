#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code

class TestDay04(unittest.TestCase):
    # Part 01
    def test_example01(self):
        secret = "abcdef"
        expected = 609043

        result = code.part01(secret)
        self.assertEqual(result, expected)

    def test_example02(self):
        secret = "pqrstuv"
        expected = 1048970

        result = code.part01(secret)
        self.assertEqual(result, expected)

    # Part 02
    pass

if __name__ == '__main__':
    unittest.main()
