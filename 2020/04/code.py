#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
from typing import List

class Validator:
    # ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm
    def __init__(self, passport: str):
        self.attributes = dict()
        for p in passport.split(" "):
            attr = p.split(':')
            self.attributes[attr[0]] = attr[1]

    def is_valid(self) -> bool:
        required_attributes = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
        tests = list(map(lambda a: a in self.attributes, required_attributes))
        return False not in tests

def part01(passports: List[str]) -> int:
    validators = list()
    passport = str()
    for i in range(len(passports)):
        line = passports[i]
        if i == len(passports) - 1:
            passport += line
            validators.append(Validator(passport))
        elif line == "":
            validators.append(Validator(passport[:-1]))
            passport = str()
        else:
            passport += line + " "

    return len(list(filter(lambda v: v.is_valid(), validators)))

def part02():
    pass

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        passports = list(map(str.strip, f.readlines()))

    start_time = time.perf_counter()
    print("Solution to Part 01 is:", part01(passports))
    part_one = time.perf_counter()
    print(f"Code took {part_one - start_time:0.8f}s to run")

    start_time = time.perf_counter()
    print("Solution to Part 02 is:", part02())
    part_two = time.perf_counter()
    print(f"Code took {part_two - start_time:0.8f}s to run")
