#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import timeit
from typing import List, Optional, Tuple, Dict


def deduce_map(row: Tuple[str]) -> Dict[int, set]:
    # Logic shamelessly stolen from https://github.com/BastianGanze/AdventOfCode2021/blob/master/08/src/main.rs
    mapping = dict()

    for i in row[:10]:
        if len(i) == 2:
            mapping['1'] = i
        elif len(i) == 3:
            mapping['7'] = i
        elif len(i) == 4:
            mapping['4'] = i
        elif len(i) == 7:
            mapping['8'] = i

    for i in row[:10]:
        if len(i) == 6:
            # if 6 segments are set and only one of the segments of 1 is set, then this is the number 6
            if len(set(i).difference(mapping['1'])) == 5:
                mapping['6'] = i
            # if 6 segments are set and all the segments of 4 are set, this is 9
            elif len(set(i).difference(mapping['4'])) == 2:
                mapping['9'] = i

    for i in row[:10]:
        # if 6 segments are set and its neither 6 nor 9 this must be 0
        if len(i) == 6 and i not in (mapping['6'], mapping['9']):
            mapping['0'] = i
        elif len(i) == 5:
            # if 5 segments are set and all 3 segments of 7 are set this is 3
            if len(set(i).difference(mapping['7'])) == 2:
                mapping['3'] = i
            # if 5 segments are set and there is exactly 1 segment difference to 6 then this is 5
            elif len(set(mapping['6']).difference(i)) == 1:
                mapping['5'] = i

    for i in row[:10]:
        if len(i) == 5:
            # Two is the only one left
            if i not in (mapping['3'], mapping['5']):
                mapping['2'] = i

    return {int(x): set(y) for x, y in mapping.items()}


def parse_input(values: Tuple[str]) -> List[List[str]]:
    return [v.removesuffix('\n').replace(' | ', ' ').split(' ') for v in values]


def part01(values: Tuple[str]) -> int:
    return len(list(filter(lambda x: x in (2, 3, 4, 7), map(len, [x for i in parse_input(values) for x in i[10:]]))))


def part02(values: Tuple[str]) -> int:
    count = 0
    for row in parse_input(values):
        mapping = deduce_map(row)
        for i in range(4):
            decoded = list(mapping.keys())[list(mapping.values()).index(set(row[10+i]))]
            count += decoded * 10**(3 - i)

    return count


if __name__ == '__main__':
    BENCH_LOOPS = 1
    BENCH_REPEAT = 10000

    with open("input.txt", "r") as f:
        data = tuple(f.readlines())

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
