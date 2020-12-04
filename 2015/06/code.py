#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys, timeit
from typing import List

import re

def part01(instructions: List[str]) -> int:
    width = 1000

    lights = [False] * width * width
    for i in instructions:
        m = re.match("^(turn on|turn off|toggle) (\d{1,3})\,(\d{1,3}) through (\d{1,3})\,(\d{1,3})", i)

        x_start, x_end = int(m.group(2)), int(m.group(4))
        y_start, y_end = int(m.group(3)), int(m.group(5))

        # Hello javidx9 ;-)
        for y in range(width):
            for x in range(width):
                if x_start <= x <= x_end and y_start <= y <= y_end:
                    cmd = m.group(1)
                    if cmd == "turn on": lights[y * width + x] = True
                    elif cmd == "turn off": lights[y * width + x] = False
                    elif cmd == "toggle": lights[y * width + x] = not lights[y * width + x]
                    else: raise ValueError("Unknown command")

    return len(list(filter(lambda x: x, lights)))

def part02():
    pass

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        instructions = list(map(lambda i: i.strip(), f.readlines()))

    print("Solution to Part One is:", part01(instructions))
    print("Solution to Part Two is:", part02())
    
    if "-b" in sys.argv:
        BENCH_LOOPS = 1
        BENCH_REPEAT = 10000

        t1 = timeit.Timer("part01(instructions)", globals=locals())
        time_p1 = min(t1.repeat(repeat=BENCH_REPEAT, number=BENCH_LOOPS))
        print(f"Part One: {BENCH_LOOPS} loops, best of {BENCH_REPEAT} repeats: {time_p1:0.8f}s")

        t2 = timeit.Timer("part02()", globals=locals())
        time_p2 = min(t2.repeat(repeat=BENCH_REPEAT, number=BENCH_LOOPS))
        print(f"Part Two: {BENCH_LOOPS} loops, best of {BENCH_REPEAT} repeats: {time_p2:0.8f}s")
