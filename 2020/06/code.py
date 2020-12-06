#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys, timeit
from typing import List

from pprint import pprint

def part01(answers: List[str]) -> int:
    return sum(map(lambda a: (len(set("".join(a)))), answers))

def part02(answers: List[str]) -> int:
    i = 0
    for a in answers:
        for c in "abcdefghijklmnopqrstuvwxyz":
            # len(e) > 0 because I'm to stupid to remove \n at EOF
            if all(c in e for e in a if len(e) > 0):
                i += 1

    return i

if __name__ == '__main__':
    BENCH_LOOPS = 1
    BENCH_REPEAT = 10000

    with open("input.txt", "r") as f:
        # [ ("abc",), ("a", "b", "c"), ("ab", "ac"), ("a", "a", "a", "a"), ("b",)]
        answers = [tuple(x.split('\n')) for x in f.read().split('\n\n')]

    if "-1" in sys.argv:
        print("Solution to Part One is:", part01(answers))

        if "-b" in sys.argv:
            t1 = timeit.Timer("part01(answers)", globals=locals())
            time_p1 = min(t1.repeat(repeat=BENCH_REPEAT, number=BENCH_LOOPS))
            print(f"Part One: {BENCH_LOOPS} loops, best of {BENCH_REPEAT} repeats: {time_p1:0.8f}s")
    elif "-2" in sys.argv:
        print("Solution to Part Two is:", part02(answers))

        if "-b" in sys.argv:
            t2 = timeit.Timer("part02(answers)", globals=locals())
            time_p2 = min(t2.repeat(repeat=BENCH_REPEAT, number=BENCH_LOOPS))
            print(f"Part Two: {BENCH_LOOPS} loops, best of {BENCH_REPEAT} repeats: {time_p2:0.8f}s")
    else:
        print("Usage: ./code.py (-1|-2) [-b]")
