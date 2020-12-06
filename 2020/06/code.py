#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys, timeit
from typing import List

def part01(answers: List[str]) -> int:
    return sum(map(lambda a: len(set("".join(a))), answers))

def part02(answers: List[str]) -> int:
    i = 0
    for a in answers:
        m = set(a[0])
        for x in a[1:]:
            m = m.intersection(x)
        i += len(m)
    return i

if __name__ == '__main__':
    BENCH_LOOPS = 1
    BENCH_REPEAT = 10000

    with open("input.txt", "r") as f:
        # [ ("abc",), ("a", "b", "c"), ("ab", "ac"), ("a", "a", "a", "a"), ("b",)]
        answers = [tuple(x.splitlines()) for x in f.read().split('\n\n')]

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
