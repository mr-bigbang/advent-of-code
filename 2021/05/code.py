#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import timeit
from typing import List, Optional, Tuple


def parse_input(values: Tuple[str]) -> List[Tuple[int, int]]:
    ret = list()
    for v in values:
        l, r = v.split(" -> ")
        ret.append((tuple(map(int, l.split(','))), tuple(map(int, r.split(',')))))

    return ret


def part01(values: Tuple[str]) -> int:
    coord = parse_input(values)
    max_x = max(max([(v[0][0], v[1][0]) for v in coord]))
    max_y = max(max([(v[0][1], v[1][1]) for v in coord]))

    width, height = max_x + 1, max_y + 1
    vents = [0] * height * width
    for c in coord:
        x_start, y_start = c[0]
        x_end, y_end = c[1]

        if x_start == x_end:
            # Vertical line
            if y_start < y_end:
                for y in range(y_start, y_end + 1):
                    vents[y * width + x_start] += 1
            else:
                for y in reversed(range(y_end, y_start + 1)):
                    vents[y * width + x_start] += 1
        elif y_start == y_end:
            # Horizontal line
            if x_start < x_end:
                for x in range(x_start, x_end + 1):
                    vents[y_start * width + x] += 1
            else:
                for x in reversed(range(x_end, x_start + 1)):
                    vents[y_start * width + x] += 1
        else:
            # Ignore for now
            pass

    return len(list(filter(lambda v: v >= 2, vents)))


def part02(values: Tuple[str]) -> int:
    pass


if __name__ == '__main__':
    BENCH_LOOPS = 1
    BENCH_REPEAT = 10000

    with open("input.txt", "r") as f:
        data = f.readlines()

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
