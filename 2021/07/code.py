#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import math
import sys
import timeit
from typing import List, Optional, Tuple


def part01(values: Tuple[int]) -> int:
    crabs = list(values)
    crabs.sort()
    median = crabs[int(len(crabs) / 2)]
    cost = sum([abs(i - median) for i in crabs])

    return cost


def part02(values):
    # This took me ages to figure out (in the end I stole it from reddit) and still don't get it fully
    #
    # I think Math says that the minimum position is between -0.5 and +0.5 of the average
    #   avg + 0.5 >= pos >= avg - 0.5
    # and we use floor/ceil for the 0.5 deviation.
    avg = sum(values) / len(values)
    floor, ceil = math.floor(avg), math.ceil(avg)
    fuel_f = sum((sum(range(1, abs(x - floor) + 1)) for x in values))
    fuel_c = sum((sum(range(1, abs(x - ceil) + 1)) for x in values))

    return fuel_f if fuel_f < fuel_c else fuel_c


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
