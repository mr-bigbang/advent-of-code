#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys, timeit
from typing import List

def part01(commands: List[str]):
    horizontal = 0
    vertical = 0

    for c in commands:
        command, amount = c.split(" ")
        if command == "forward":
            horizontal += int(amount)
        elif command == "down":
            vertical += int(amount)
        elif command == "up":
            vertical -= int(amount)

    return horizontal * vertical

def part02(commands: List[str]):
    horizontal = 0
    vertical = 0
    aim = 0

    for c in commands:
        command, amount = c.split(" ")
        amount = int(amount)
        if command == "forward":
            horizontal += amount
            vertical += aim * amount
        elif command == "down":
            aim += amount
        elif command == "up":
            aim -= amount

    return horizontal * vertical

if __name__ == '__main__':
    BENCH_LOOPS = 1
    BENCH_REPEAT = 10000

    with open("input.txt", "r") as f:
        commands = list(f.readlines())

    if "-1" in sys.argv:
        print("Solution to Part One is:", part01(commands))

        if "-b" in sys.argv:
            t1 = timeit.Timer("part01(commands)", globals=locals())
            time_p1 = min(t1.repeat(repeat=BENCH_REPEAT, number=BENCH_LOOPS))
            print(f"Part One: {BENCH_LOOPS} loops, best of {BENCH_REPEAT} repeats: {time_p1:0.8f}s")
    elif "-2" in sys.argv:
        print("Solution to Part Two is:", part02(commands))

        if "-b" in sys.argv:
            t2 = timeit.Timer("part02(commands)", globals=locals())
            time_p2 = min(t2.repeat(repeat=BENCH_REPEAT, number=BENCH_LOOPS))
            print(f"Part Two: {BENCH_LOOPS} loops, best of {BENCH_REPEAT} repeats: {time_p2:0.8f}s")
    else:
        print("Usage: ./code.py (-1|-2) [-b]")
