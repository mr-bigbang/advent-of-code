#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import timeit
from typing import List, Optional, Tuple


def simulate(values: Tuple[int], days: int) -> int:
    # Number of fish by age
    fish = [values.count(i) for i in range(9)]
    for _ in range(days):
        new_fish = [0] * 9

        # Age all fish
        for i in range(1, 9):
            new_fish[i-1] = fish[i]

        # Produce new fish
        new_fish[8] = fish[0]
        new_fish[6] += fish[0]

        fish = new_fish
    return sum(fish)


def part01(values: Tuple[int]) -> int:
    return simulate(values, 80)


def part02(values: Tuple[int]) -> int:
    return simulate(values, 256)


if __name__ == '__main__':
    BENCH_LOOPS = 1
    BENCH_REPEAT = 10000

    with open("input.txt", "r") as f:
        data = tuple(map(int, f.read().split(',')))

    if "-1" in sys.argv:
        print("Solution to Part One is:", part01(data))

        if "-b" in sys.argv:
            t1 = timeit.Timer("part01(data)", globals=locals())
            time_p1 = min(t1.repeat(repeat=BENCH_REPEAT, number=BENCH_LOOPS))
            print(f"Part One: {BENCH_LOOPS} loops, best of {BENCH_REPEAT} repeats: {time_p1:0.8f}s")
    elif "-2" in sys.argv:
        print("Solution to Part Two is:", part02(data))

        if "-b" in sys.argv:
            t2 = timeit.Timer("part02(data)", globals=locals())
            time_p2 = min(t2.repeat(repeat=BENCH_REPEAT, number=BENCH_LOOPS))
            print(f"Part Two: {BENCH_LOOPS} loops, best of {BENCH_REPEAT} repeats: {time_p2:0.8f}s")
    else:
        print("Usage: ./code.py (-1|-2) [-b]")
