#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code


class TestDayXX(unittest.TestCase):
    def setUp(self) -> None:
        pass

    # Part 01
    def test_example01(self):
        expected = None

        result = code.part01()
        self.assertEqual(expected, result)

    # Part 02
    def test_example02(self):
        expected = None

        result = code.part01()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
