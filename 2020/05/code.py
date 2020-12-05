#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys, timeit
from typing import List, Tuple

def get_seat(bp: str) -> Tuple[int, int]:
    # TODO I think this would be fun with recursion
    rows = [x for x in range(128)]
    for r in bp[:7]:
        s = len(rows) // 2
        rows = rows[:s] if r == "F" else rows[s:]

    cols = [x for x in range(8)]
    for c in bp[7:]:
        s = len(cols) // 2
        cols = cols[:s] if c == "L" else cols[s:]

    return (rows[0], cols[0])

def get_seat_id(seat: Tuple[int, int]) -> int:
    return seat[0] * 8 + seat[1]

def part01(boarding_passes: List[str]) -> int:
    return max(map(get_seat_id, map(get_seat, boarding_passes)))

def part02(boarding_passes: List[str]) -> int:
    seats = sorted(map(get_seat_id, map(get_seat, boarding_passes)))
    # I don't have much time today
    # So we use simple for loop
    for s in seats:
        if s + 1 not in seats:
            return s + 1

if __name__ == '__main__':
    BENCH_LOOPS = 1
    BENCH_REPEAT = 10000

    with open("input.txt", "r") as f:
        boarding_passes = f.read().strip().split('\n')

    if "-1" in sys.argv:
        print("Solution to Part One is:", part01(boarding_passes))

        if "-b" in sys.argv:
            t1 = timeit.Timer("part01(boarding_passes)", globals=locals())
            time_p1 = min(t1.repeat(repeat=BENCH_REPEAT, number=BENCH_LOOPS))
            print(f"Part One: {BENCH_LOOPS} loops, best of {BENCH_REPEAT} repeats: {time_p1:0.8f}s")
    elif "-2" in sys.argv:
        print("Solution to Part Two is:", part02(boarding_passes))

        if "-b" in sys.argv:
            t2 = timeit.Timer("part02(boarding_passes)", globals=locals())
            time_p2 = min(t2.repeat(repeat=BENCH_REPEAT, number=BENCH_LOOPS))
            print(f"Part Two: {BENCH_LOOPS} loops, best of {BENCH_REPEAT} repeats: {time_p2:0.8f}s")
    else:
        print("Usage: ./code.py (-1|-2) [-b]")
