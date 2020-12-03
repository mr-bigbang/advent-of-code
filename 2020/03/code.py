#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
from typing import List

def part01(geology: List[str]) -> int:
    slope = (3, 1)
    position = [0, 0]
    trees = 0

    while position[1] < len(geology):
        row = geology[position[1]]
        if row[position[0]] == '#':
            trees += 1

        # Add slope to position
        position = [position[0] + slope[0], position[1] + slope[1]]

        # Wrap X-Axis
        if position[0] >= len(row):
            position[0] -= len(row)

    return trees

def part02():
    pass

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        geology = list(map(str.strip, f.readlines()))

    start_time = time.perf_counter()
    print("Solution to Part 01 is:", part01(geology))
    part_one = time.perf_counter()
    print(f"Code took {part_one - start_time:0.8f}s to run")

    start_time = time.perf_counter()
    print("Solution to Part 02 is:", part02())
    part_two = time.perf_counter()
    print(f"Code took {part_two - start_time:0.8f}s to run")
