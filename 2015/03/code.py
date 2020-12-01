#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
# from typing import List
import itertools

def part01(directions: str) -> int:
    # North-South & East-West Coordinates
    ns, ew = 0, 0
    # Origin is always visited
    visited_coords = [[ns, ew], ]
    for d in directions:
        if d == "^":
            ns += 1
        elif d == "v":
            ns -= 1
        elif d == "<":
            ew -= 1
        elif d == ">":
            ew += 1
        else:
            pass

        visited_coords.append([ns, ew])

    # Remove duplicates
    visited_coords.sort()
    return len([c for c,_ in itertools.groupby(visited_coords)])

def part02():
    pass

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        directions = f.read()

    start_time = time.perf_counter()
    print("Solution to Part 01 is:", part01(directions))
    part_one = time.perf_counter()
    print(f"Code took {part_one - start_time:0.8f}s to run")

    start_time = time.perf_counter()
    print("Solution to Part 02 is:", part02())
    part_two = time.perf_counter()
    print(f"Code took {part_two - start_time:0.8f}s to run")
