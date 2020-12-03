#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
from typing import List, Tuple

def get_trees(geology: List[str], slope: Tuple[int, int]) -> int:
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

def part01(geology: List[str]) -> int:
    return get_trees(geology, (3, 1))

def part02(geology: List[str]) -> int:
    return get_trees(geology, (1, 1)) * \
           get_trees(geology, (3, 1)) * \
           get_trees(geology, (5, 1)) * \
           get_trees(geology, (7, 1)) * \
           get_trees(geology, (1, 2))

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
