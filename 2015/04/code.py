#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
# from typing import List
from hashlib import md5

def test_hash(secret, number, zeros = 5) -> bool:
    return md5(f"{secret}{number}".encode()).hexdigest()[:zeros] == '0' * zeros

def part01(secret: str) -> int:
#    return next(filter(lambda x: test_hash(secret, x), range(10**100)))
    i = 1
    while True:
        if test_hash(secret, i):
            return i
        else:
            i += 1

def part02(secret: str) -> int:
    i = 1
    while True:
        if test_hash(secret, i, 6):
            return i
        else:
            i += 1

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        secret = f.read().strip()

    start_time = time.perf_counter()
    print("Solution to Part 01 is:", part01(secret))
    part_one = time.perf_counter()
    print(f"Code took {part_one - start_time:0.8f}s to run")

    start_time = time.perf_counter()
    print("Solution to Part 02 is:", part02(secret))
    part_two = time.perf_counter()
    print(f"Code took {part_two - start_time:0.8f}s to run")
