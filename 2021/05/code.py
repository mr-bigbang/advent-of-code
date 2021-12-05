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


def flatten_coords(values) -> List[Tuple[int, int]]:
    ret = []
    for v in values:
        x, y, xx, yy = v[0] + v[1]
        if x == xx:
            # Horizontal line
            ret += [(x, i) for i in range(min(y, yy), max(y, yy) + 1)]
        elif y == yy:
            # Vertical line
            ret += [(i, y) for i in range(min(x, xx), max(x, xx) + 1)]
        else:
            # Ignore for now
            pass

    return ret


def part01(values: Tuple[str]) -> int:
    flat_coords = flatten_coords(parse_input(values))
    max_x = max([c[0] for c in flat_coords])
    max_y = max([c[1] for c in flat_coords])

    width, height = max_x + 1, max_y + 1
    vents = [0] * height * width
    for c in flat_coords:
        vents[c[1] * width + c[0]] += 1

    return len(list(filter(lambda v: v > 1, vents)))


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
