#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
from typing import List

class Validator:
    def __init__(self, passport: str):
        self.attributes = dict([p.split(':') for p in passport.strip().split(" ")])

    def is_valid(self) -> bool:
        required_attributes = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
        tests = list(map(lambda a: a in self.attributes, required_attributes))
        return False not in tests

    def is_still_valid(self) -> bool:
        if self.is_valid():
            byr = 1920 <= int(self.attributes['byr']) <= 2002
            iyr = 2010 <= int(self.attributes['iyr']) <= 2020
            eyr = 2020 <= int(self.attributes['eyr']) <= 2030
            hgt = 150 <= int(self.attributes['hgt'][:-2]) <= 193 if "cm" in self.attributes['hgt'] else 59 <= int(self.attributes['hgt'][:-2]) <= 76
            hcl = self.attributes['hcl'][0] == '#' and int(self.attributes['eyr'][1:], 16)
            ecl = self.attributes['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
            pid = len(self.attributes['pid']) == 9

            return False not in (byr, iyr, eyr, hgt, hcl, ecl, pid)
        else:
            return False

def part01(passports: List[str]) -> int:
    return len(list(filter(lambda v: v.is_valid(), map(lambda p: Validator(p), passports))))

def part02(passports: List[str]) -> int:
    return len(list(filter(lambda v: v.is_still_valid(), map(lambda p: Validator(p), passports))))

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        passports = [l.replace('\n', ' ') for l in f.read().split('\n\n')]

    start_time = time.perf_counter()
    print("Solution to Part 01 is:", part01(passports))
    part_one = time.perf_counter()
    print(f"Code took {part_one - start_time:0.8f}s to run")

    start_time = time.perf_counter()
    print("Solution to Part 02 is:", part02(passports))
    part_two = time.perf_counter()
    print(f"Code took {part_two - start_time:0.8f}s to run")
