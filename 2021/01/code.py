#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys, timeit
from typing import List

def part01(input: List[int]):
    result = 0
    last_measure = 0

    for measure in input:
        if measure > last_measure:
            result += 1
        last_measure = measure
    return result - 1 # The first measurement is not counted

def part02(input: List[int]):
    result = 0
    last_measure = 0

    # The last two items are never the start of a sliding window
    for i in range(len(input) - 2):
        measure = sum(input[i:i+3])
        if measure > last_measure:
            result += 1
        last_measure = measure
    return result - 1 # The first measurement is not counted

if __name__ == '__main__':
    BENCH_LOOPS = 1
    BENCH_REPEAT = 10000

    with open("input.txt", "r") as f:
        input = list(map(int, f.readlines()))

    if "-1" in sys.argv:
        print("Solution to Part One is:", part01(input))

        if "-b" in sys.argv:
            t1 = timeit.Timer("part01(input)", globals=locals())
            time_p1 = min(t1.repeat(repeat=BENCH_REPEAT, number=BENCH_LOOPS))
            print(f"Part One: {BENCH_LOOPS} loops, best of {BENCH_REPEAT} repeats: {time_p1:0.8f}s")
    elif "-2" in sys.argv:
        print("Solution to Part Two is:", part02(input))

        if "-b" in sys.argv:
            t2 = timeit.Timer("part02(input)", globals=locals())
            time_p2 = min(t2.repeat(repeat=BENCH_REPEAT, number=BENCH_LOOPS))
            print(f"Part Two: {BENCH_LOOPS} loops, best of {BENCH_REPEAT} repeats: {time_p2:0.8f}s")
    else:
        print("Usage: ./code.py (-1|-2) [-b]")
