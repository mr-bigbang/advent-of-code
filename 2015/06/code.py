#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys, timeit
from typing import List

import re

def part01(instructions: List[str]) -> int:
    width = 1000

    lights = [False] * width * width
    pattern = re.compile("^(turn on|turn off|toggle) (\d{1,3})\,(\d{1,3}) through (\d{1,3})\,(\d{1,3})$")
    for i in instructions:
        m = pattern.match(i)

        cmd = m.group(1)
        x_start, x_end = int(m.group(2)), int(m.group(4))
        y_start, y_end = int(m.group(3)), int(m.group(5))

        # Hello javidx9 ;-)
        for y in range(y_start, y_end + 1):
            for x in range(x_start, x_end + 1):
                if cmd == "turn on": lights[y * width + x] = True
                elif cmd == "turn off": lights[y * width + x] = False
                elif cmd == "toggle": lights[y * width + x] = not lights[y * width + x]
                else: raise ValueError("Unknown command")

    return len(list(filter(lambda x: x, lights)))

def part02(instructions: List[str]) -> int:
    width = 1000

    lights = [0] * width * width
    pattern = re.compile("^(turn on|turn off|toggle) (\d{1,3})\,(\d{1,3}) through (\d{1,3})\,(\d{1,3})$")
    for i in instructions:
        m = pattern.match(i)

        cmd = m.group(1)
        x_start, x_end = int(m.group(2)), int(m.group(4))
        y_start, y_end = int(m.group(3)), int(m.group(5))

        # Hello again, javidx9 ;-)
        for y in range(y_start, y_end + 1):
            for x in range(x_start, x_end + 1):
                if cmd == "turn on":
                    lights[y * width + x] += 1
                elif cmd == "turn off":
                    lights[y * width + x] -= 1 if lights[y * width + x] > 0 else 0
                elif cmd == "toggle":
                    lights[y * width + x] += 2
                else:
                    raise ValueError("Unknown command")

    return sum(lights)

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        instructions = list(map(lambda i: i.strip(), f.readlines()))

    print("Solution to Part One is:", part01(instructions))
    print("Solution to Part Two is:", part02(instructions))
    
    if "-b" in sys.argv:
        BENCH_LOOPS = 1
        BENCH_REPEAT = 10

        t1 = timeit.Timer("part01(instructions)", globals=locals())
        time_p1 = min(t1.repeat(repeat=BENCH_REPEAT, number=BENCH_LOOPS))
        print(f"Part One: {BENCH_LOOPS} loops, best of {BENCH_REPEAT} repeats: {time_p1:0.8f}s")

        t2 = timeit.Timer("part02(instructions)", globals=locals())
        time_p2 = min(t2.repeat(repeat=BENCH_REPEAT, number=BENCH_LOOPS))
        print(f"Part Two: {BENCH_LOOPS} loops, best of {BENCH_REPEAT} repeats: {time_p2:0.8f}s")
