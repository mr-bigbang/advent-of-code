#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code

class TestDay02(unittest.TestCase):
    def setUp(self) -> None:
        self.commands = [
                "forward 5",
                "down 5",
                "forward 8",
                "up 3",
                "down 8",
                "forward 2"]

    # Part 01
    def test_example01(self):
        expected = 150

        result = code.part01(self.commands)
        self.assertEqual(result, expected)

    # Part 02
    def test_example02(self):
        expected = 900

        result = code.part02(self.commands)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
