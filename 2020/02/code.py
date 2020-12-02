#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
from typing import List

class Validator:
    def __init__(self, entry):
        pol, pw = entry.split(':')
        occ, char = pol.split(' ')
        low, high = occ.split('-')

        self.low = int(low)
        self.high = int(high)
        self.char = char
        self.pw = pw.strip()

    def valid(self):
        occ = self.pw.count(self.char)
        return occ >= self.low and occ <= self.high

    def valid_pos(self):
        return (self.pw[self.low - 1] == self.char) ^ (self.pw[self.high - 1] == self.char)

def part01(passwords: List[str]) -> int:
    # Create Validator instance for all password entries
    validators = map(lambda x: Validator(x), passwords)

    # Call valid() on each Validator instance, dropping invalid
    valid_passwords = filter(lambda pw: pw.valid(), validators)

    return(len(list(valid_passwords)))

def part02(passwords: List[str]) -> int:
    # Create Validator instance for all password entries
    validators = map(lambda x: Validator(x), passwords)

    # Call valid_pos() on each Validator instance, dropping invalid
    valid_passwords = filter(lambda pw: pw.valid_pos(), validators)

    return(len(list(valid_passwords)))

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        passwords = f.readlines()

    start_time = time.perf_counter()
    print("Solution to Part 01 is:", part01(passwords))
    part_one = time.perf_counter()
    print(f"Code took {part_one - start_time:0.8f}s to run")

    start_time = time.perf_counter()
    print("Solution to Part 02 is:", part02(passwords))
    part_two = time.perf_counter()
    print(f"Code took {part_two - start_time:0.8f}s to run")
