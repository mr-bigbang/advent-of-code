#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
from typing import List

def is_nice(string: str) -> bool:
    # Condition 3
    if False not in [s not in string for s in ('ab', 'cd', 'pq', 'xy')]:
        # Condition 2
        if True in [f"{c}{c}" in string for c in string]:
            # Condition 1
            if len(list(filter(lambda c: c in "aeiou", string))) >= 3:
                return True
    
    return False

def part01(strings: List[str]) -> int:
    return len(list(filter(is_nice, strings)))

def part02():
    pass

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        strings = list(map(str.strip, f.readlines()))

    start_time = time.perf_counter()
    print("Solution to Part 01 is:", part01(strings))
    part_one = time.perf_counter()
    print(f"Code took {part_one - start_time:0.8f}s to run")

    start_time = time.perf_counter()
    print("Solution to Part 02 is:", part02())
    part_two = time.perf_counter()
    print(f"Code took {part_two - start_time:0.8f}s to run")
