#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code

class TestDay06(unittest.TestCase):
    # Part 01
    def test_example01(self):
        answers = [("abc",),
                   ("a", "b", "c"),
                   ("ab", "ac"),
                   ("a", "a", "a", "a"),
                   ("b")]
        expected = 11

        result = code.part01(answers)
        self.assertEqual(result, expected)

    # Part 02
    def test_example02(self):
        answers = [("abc",),
                   ("a", "b", "c"),
                   ("ab", "ac"),
                   ("a", "a", "a", "a"),
                   ("b")]
        expected = 6

        result = code.part02(answers)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
