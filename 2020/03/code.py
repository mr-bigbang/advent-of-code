#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
from typing import List, Tuple
from functools import reduce

def get_trees(geology: List[str], slope: Tuple[int, int]) -> int:
    x, y = 0, 0
    trees = 0

    width = len(geology[0])
    while y < len(geology):
        row = geology[y]
        trees += 1 if row[x] == '#' else 0

        # Add slope to position and wrap x-axis
        x = (x + slope[0]) % width
        y += slope[1]

    return trees

def part01(geology: List[str]) -> int:
    return get_trees(geology, (3, 1))

def part02(geology: List[str]) -> int:
    slopes = ((1,1), (3,1), (5,1), (7,1), (1,2))
    return reduce(lambda x, y: x * y, [get_trees(geology, s) for s in slopes])

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        geology = list(map(str.strip, f.readlines()))

    start_time = time.perf_counter()
    print("Solution to Part 01 is:", part01(geology))
    part_one = time.perf_counter()
    print(f"Code took {part_one - start_time:0.8f}s to run")

    start_time = time.perf_counter()
    print("Solution to Part 02 is:", part02(geology))
    part_two = time.perf_counter()
    print(f"Code took {part_two - start_time:0.8f}s to run")
