#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys, timeit
# from typing import List

def part01():
    pass

def part02():
    pass

if __name__ == '__main__':
    BENCH_LOOPS = 1
    BENCH_REPEAT = 10000

    with open("input.txt", "r") as f:
        pass

    if "-1" in sys.argv:
        print("Solution to Part One is:", part01())

        if "-b" in sys.argv:
            t1 = timeit.Timer("part01()", globals=locals())
            time_p1 = min(t1.repeat(repeat=BENCH_REPEAT, number=BENCH_LOOPS))
            print(f"Part One: {BENCH_LOOPS} loops, best of {BENCH_REPEAT} repeats: {time_p1:0.8f}s")
    elif "-2" in sys.argv:
        print("Solution to Part Two is:", part02())

        if "-b" in sys.argv:
            t2 = timeit.Timer("part02()", globals=locals())
            time_p2 = min(t2.repeat(repeat=BENCH_REPEAT, number=BENCH_LOOPS))
            print(f"Part Two: {BENCH_LOOPS} loops, best of {BENCH_REPEAT} repeats: {time_p2:0.8f}s")
    else:
        print("Usage: ./code.py (-1|-2) [-b]")
