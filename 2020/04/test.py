#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code

class TestDay04(unittest.TestCase):
    def setUp(self):
        self.passports = ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
                          "byr:1937 iyr:2017 cid:147 hgt:183cm",
                          "",
                          "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
                          "hcl:#cfa07d byr:1929",
                          "",
                          "hcl:#ae17e1 iyr:2013",
                          "eyr:2024",
                          "ecl:brn pid:760753108 byr:1931",
                          "hgt:179cm",
                          "",
                          "hcl:#cfa07d eyr:2025 pid:166559648",
                          "iyr:2011 ecl:brn hgt:59in"]

    # Part 01
    def test_example01(self):
        expected = 2

        result = code.part01(self.passports)
        self.assertEqual(result, expected)

    # Part 02
    pass

if __name__ == '__main__':
    unittest.main()
