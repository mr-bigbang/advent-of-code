#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code

class TestDay01(unittest.TestCase):
    def test_example01(self):
        expense_report = [1721, 299]
        expected = 514579

        result = code.part01(expense_report)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
