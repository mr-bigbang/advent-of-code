#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code


class TestDay03(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [
            0b00100,
            0b11110,
            0b10110,
            0b10111,
            0b10101,
            0b01111,
            0b00111,
            0b11100,
            0b10000,
            0b11001,
            0b00010,
            0b01010,
        ]

    # Part 01
    def test_example01(self):
        expected = 198

        result = code.part01(self.data)
        self.assertEqual(expected, result)

    # Part 02
    def test_example02(self):
        expected = 230

        result = code.part02(self.data)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
