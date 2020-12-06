#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code

class TestDay06(unittest.TestCase):
    # Part 01
    def test_example01(self):
        answers = ["abc",
                   "abc",
                   "abac",
                   "aaaa",
                   "b"]
        expected = 11

        result = code.part01(answers)
        self.assertEqual(result, expected)

    # Part 02
    pass

if __name__ == '__main__':
    unittest.main()
