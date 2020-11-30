#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest

import code

class TestDay01(unittest.TestCase):
    # Part One
    def test_example01(self):
        for s in ["(())", "()()"]:
            with self.subTest(s):
                floor = code.part01(s)
                self.assertEqual(floor, 0)

    def test_example02(self):
        for s in ["(((", "(()(()("]:
            with self.subTest(s):
                floor = code.part01(s)
                self.assertEqual(floor, 3)

    def test_example03(self):
        for s in ["))((((("]:
            with self.subTest(s):
                floor = code.part01(s)
                self.assertEqual(floor, 3)

    def test_example04(self):
        for s in ["())", "))("]:
            with self.subTest(s):
                floor = code.part01(s)
                self.assertEqual(floor, -1)

    def test_example05(self):
        for s in [")))", ")())())"]:
            with self.subTest(s):
                floor = code.part01(s)
                self.assertEqual(floor, -3)

    # Part Two
    def test_example06(self):
        position = code.part02(")")
        self.assertEqual(position, 1)


    def test_example07(self):
        position = code.part02("()())")
        self.assertEqual(position, 5)

if __name__ == '__main__':
    unittest.main()
