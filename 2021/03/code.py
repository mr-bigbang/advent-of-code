#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys, timeit
from typing import Tuple, List, Optional

def part01(diagnostics: Tuple[int]) -> int:
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


def most_common(values, pos) -> Optional[bool]:
    counter = 0
    for v in values:
        if v & (1 << pos) == (1 << pos):
            counter += 1
        else:
            counter -= 1

    return None if counter == 0 else counter > 0


def least_common(values, pos) -> Optional[bool]:
    mc = most_common(values, pos)
    return None if mc is None else not mc


def one_at_pos(value: int, pos: int) -> bool:
    return value & (1 << pos) > 0


def oxygen_generator_rating(values: List[int]):
    num_bits = max(values).bit_length()
    for i in range(num_bits - 1, -1, -1):
        if len(values) == 1:
            break

        if most_common(values, i) == 0:
            values = list(filter(lambda x: not one_at_pos(x, i), values))
        else:
            values = list(filter(lambda x: one_at_pos(x, i), values))

    return values[0]


def co2_scrubber_rating(values: List[int]):
    num_bits = max(values).bit_length()
    for i in range(num_bits - 1, -1, -1):
        if len(values) == 1:
            break

        if least_common(values, i) == 1:
            values = list(filter(lambda x: one_at_pos(x, i), values))
        else:
            values = list(filter(lambda x: not one_at_pos(x, i), values))

    return values[0]


def part02(diagnostics: Tuple[int]) -> int:
    return oxygen_generator_rating(diagnostics) * co2_scrubber_rating(diagnostics)


if __name__ == '__main__':
    BENCH_LOOPS = 1
    BENCH_REPEAT = 10000

    with open("input.txt", "r") as f:
        data = tuple(map(lambda x: int(x, 2), f.readlines()))

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
