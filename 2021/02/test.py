#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code

class TestDay02(unittest.TestCase):
    # Part 01
    def test_example01(self):
        commands = [
                "forward 5",
                "down 5",
                "forward 8",
                "up 3",
                "down 8",
                "forward 2"]
        expected = 150

        result = code.part01(commands)
        self.assertEqual(result, expected)

    # Part 02
    pass

if __name__ == '__main__':
    unittest.main()
