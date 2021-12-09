#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code


class TestDay08(unittest.TestCase):
    def setUp(self):
        self.data = (
            "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
            "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
            "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
            "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
            "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
            "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
            "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
            "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
            "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
            "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
        )

        self.data1 = (
            "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf",
        )

        with open("input.txt", "r") as f:
            self.input = tuple(f.readlines())

    # Part 01
    def test_example01(self):
        expected = 26

        result = code.part01(self.data)
        self.assertEqual(expected, result)

    def test_result01(self):
        expected = 504

        result = code.part01(self.input)
        self.assertEqual(expected, result)

    # Part 02
    def test_example02(self):
        expected = 5353

        result = code.part02(self.data1)
        self.assertEqual(expected, result)

    def test_example03(self):
        expected = 61229

        result = code.part02(self.data)
        self.assertEqual(expected, result)

    def test_result02(self):
        expected = 1073431

        result = code.part02(self.input)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
