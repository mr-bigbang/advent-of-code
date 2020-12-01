#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
from typing import List

def part01(presents: List[str]) -> int:
    packaging = 0
    for p in presents:
        l, w, h = map(int, p.split('x'))

        # 2*l*w + 2*w*h + 2*h*l + area_of_smallest_side
        dim = [l, w, h]
        dim.remove(max(dim))

        packaging += (2 * l * w) + (2 * w * h) + (2 * h * l) + (dim[0] * dim[1])

    return packaging

def part02():
    pass

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        presents = f.readlines()

    start_time = time.perf_counter()
    print("Solution to Part 01 is:", part01(presents))
    part_one = time.perf_counter()
    print(f"Code took {part_one - start_time:0.8f}s to run")

    start_time = time.perf_counter()
    print("Solution to Part 02 is:", part02())
    part_two = time.perf_counter()
    print(f"Code took {part_two - start_time:0.8f}s to run")
