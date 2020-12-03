#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code

class TestDay05(unittest.TestCase):
    # Part 01
    def test_example01(self):
        string = "ugknbfddgicrmopn"

        result = code.is_nice(string)
        self.assertTrue(result)

    def test_example02(self):
        string = "aaa"

        result = code.is_nice(string)
        self.assertTrue(result)

    def test_example03(self):
        string = "jchzalrnumimnmhp"

        result = code.is_nice(string)
        self.assertFalse(result)

    def test_example04(self):
        string = "haegwjzuvuyypxyu"

        result = code.is_nice(string)
        self.assertFalse(result)

    def test_example05(self):
        string = "dvszwmarrgswjxmb"

        result = code.is_nice(string)
        self.assertFalse(result)

    # Part 02
    pass

if __name__ == '__main__':
    unittest.main()
