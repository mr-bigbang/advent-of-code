#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys, timeit
from typing import List

def part01(diagnostics: List[int]):
    num_bits = max(diagnostics).bit_length()

    counter = [0] * num_bits
    for d in diagnostics:
        # counter = [counter[b] + 1 if d & (1 << b) == (1 << b) else counter[b] - 1 for b in range(num_bits)]
        for b in range(num_bits):
            if d & (1 << b) == (1 << b):
                counter[b] += 1
            else:
                counter[b] -= 1

    gamma_rate = 0
    epsilon_rate = 0
    for i in range(len(counter)):
        if counter[i] > 0:
            gamma_rate |= (1 << i)
        else:
            epsilon_rate |= (1 << i)

    return gamma_rate * epsilon_rate

def part02():
    pass

if __name__ == '__main__':
    BENCH_LOOPS = 1
    BENCH_REPEAT = 10000

    with open("input.txt", "r") as f:
        data = list(map(lambda x: int(x, 2), f.readlines()))

    if "-1" in sys.argv:
        print("Solution to Part One is:", part01(data))

        if "-b" in sys.argv:
            t1 = timeit.Timer("part01(data)", globals=locals())
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
