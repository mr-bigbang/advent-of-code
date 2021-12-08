#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import timeit
from typing import List, Optional, Tuple


def parse_input(values: Tuple[str]) -> List[Tuple[int, int]]:
    # 1 loops, best of 10000 repeats: 0.00061935s
    ret = list()
    for v in values:
        l, r = v.split(" -> ")
        ret.append((tuple(map(int, l.split(','))), tuple(map(int, r.split(',')))))

    return ret


def flatten_coordinates(values, ignore_diagonals: bool) -> List[Tuple[int, int]]:
    # Create a list with all hit coordinates
    # ignore_diagonals = True:  1 loops, best of 10000 repeats: 0.00736938s
    # ignore_diagonals = False: 1 loops, best of 10000 repeats: 0.01770101s

    def offset(x1, x2):
        return int(x1 < x2) - int(x1 > x2)

    ret = list()
    for v in values:
        x, y, xx, yy = v[0] + v[1]
        if x == xx:
            # Horizontal line
            ret += [(x, i) for i in range(min(y, yy), max(y, yy) + 1)]
        elif y == yy:
            # Vertical line
            ret += [(i, y) for i in range(min(x, xx), max(x, xx) + 1)]
        else:
            # Diagonal line
            if not ignore_diagonals:
                # Stolen from https://git.kageru.moe/kageru/advent-of-code/src/branch/master/2021/src/bin/day05.rs
                x_off = offset(x, xx)
                y_off = offset(y, yy)
                while True:
                    ret.append((x, y))
                    if x == xx and y == yy:
                        break
                    x += x_off
                    y += y_off

    return ret


def get_vents(flat_coordinates: List[Tuple[int, int]]):
    # ignore_diagonals = True:  1 loops, best of 10000 repeats: 0.07672771s
    # ignore_diagonals = False: 1 loops, best of 10000 repeats: 0.09608512s

    max_x = max([c[0] for c in flat_coordinates])  # 0.006s / 2 perf hit
    max_y = max([c[1] for c in flat_coordinates])  # 0.006s / 2 perf hit

    width, height = max_x + 1, max_y + 1
    vents = [0] * height * width
    for c in flat_coordinates:  # 0.017s perf hit (whole loop)
        vents[c[1] * width + c[0]] += 1

    return len(list(filter(lambda v: v > 1, vents)))  # 0.053s perf hit


def part01(values: Tuple[str]) -> int:
    coordinates = parse_input(values)
    flat_coordinates = flatten_coordinates(coordinates, True)
    return get_vents(flat_coordinates)


def part02(values: Tuple[str]) -> int:
    coordinates = parse_input(values)
    flat_coordinates = flatten_coordinates(coordinates, False)
    return get_vents(flat_coordinates)


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
