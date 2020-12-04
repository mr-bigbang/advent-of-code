#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code

class TestDay04(unittest.TestCase):
    def setUp(self):
        self.passports = ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm",
                          "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929",
                          "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm",
                          "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in"]

        self.part02_invalid = [
            "eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
            "iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946",
            "hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
            "hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007"]

        self.part02_valid = [
            "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",
            "eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
            "hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022",
            "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"]

    # Part 01
    def test_example01(self):
        expected = 2

        result = code.part01(self.passports)
        self.assertEqual(result, expected)
    
    def test_example01_0(self):
        result = code.Validator(self.passports[0]).is_valid()
        self.assertTrue(result)

    def test_example01_1(self):
        result = code.Validator(self.passports[1]).is_valid()
        self.assertFalse(result)

    def test_example01_2(self):
        result = code.Validator(self.passports[2]).is_valid()
        self.assertTrue(result)

    def test_example01_3(self):
        result = code.Validator(self.passports[3]).is_valid()
        self.assertFalse(result)

    # Part 02
    def test_example02(self):
        expected = 0

        result = code.part02(self.part02_invalid)
        self.assertEqual(result, expected)

    def test_example02_single(self):
        for p in self.part02_invalid:
            with self.subTest(p):
                result = code.Validator(p).is_still_valid()
                self.assertFalse(result)

    def test_example03(self):
        expected = 4

        result = code.part02(self.part02_valid)
        self.assertEqual(result, expected)

    def test_example03_single(self):
        for p in self.part02_valid:
            with self.subTest(p):
                result = code.Validator(p).is_still_valid()
                self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
