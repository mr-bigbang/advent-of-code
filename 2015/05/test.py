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
    def test_example06(self):
        string = "qjhvhtzxzqqjkmpb"

        result = code.is_still_nice(string)
        self.assertTrue(result)

    def test_example07(self):
        string = "xxyxx"

        result = code.is_still_nice(string)
        self.assertTrue(result)

    def test_example08(self):
        string = "uurcxstgmygtbstg"

        result = code.is_still_nice(string)
        self.assertFalse(result)

    def test_example09(self):
        string = "ieodomkazucvgmuy"

        result = code.is_still_nice(string)
        self.assertFalse(result)

    def test_triples(self):
        string = "qpnxkuldeiituggg"

        result = code.is_still_nice(string)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
