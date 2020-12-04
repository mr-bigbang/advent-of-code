#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
from typing import List

def is_nice(string: str) -> bool:
    if False not in [s not in string for s in ('ab', 'cd', 'pq', 'xy')]:
        if True in [ 2*c in string for c in string]:
            if len(list(filter(lambda c: c in "aeiou", string))) >= 3:
                return True
    
    return False

def is_still_nice(string: str) -> bool:
    cond1 = filter(lambda x: string.find(string[x:x+2], x+2) != -1, range(len(string)))
    cond2 = filter(lambda x: string[x] == string[x+2], range(len(string) - 2))
    return len(list(zip(cond1, cond2))) > 0

def part01(strings: List[str]) -> int:
    return len(list(filter(is_nice, strings)))

def part02(strings: List[str]) -> int:
    return len(list(filter(is_still_nice, strings)))

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        strings = list(map(str.strip, f.readlines()))

    start_time = time.perf_counter()
    print("Solution to Part 01 is:", part01(strings))
    part_one = time.perf_counter()
    print(f"Code took {part_one - start_time:0.8f}s to run")

    start_time = time.perf_counter()
    print("Solution to Part 02 is:", part02(strings))
    part_two = time.perf_counter()
    print(f"Code took {part_two - start_time:0.8f}s to run")
