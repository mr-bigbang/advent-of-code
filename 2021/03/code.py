#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys, timeit
from typing import Tuple


def bit_at(value: int, pos: int) -> bool:
    return value & (1 << pos) != 0
    # -or-
    #return (value >> pos) & 1 != 0


def most_common(values: Tuple[int], pos: int) -> bool:
    # This looks nicer but is ~3x slower :-(
    # $ ./code.py -1 -b
    # Part One: 1 loops, best of 10000 repeats: 0.00258914s
    # $ ./code.py -2 -b
    # Part Two: 1 loops, best of 10000 repeats: 0.00175088s
    #return len(list(filter(lambda x: bit_at(x, pos), values))) * 2 >= len(values)

    # Why is this faster?
    # $ ./code.py -1 -b
    # Part One: 1 loops, best of 10000 repeats: 0.00085089s
    # $ ./code.py -2 -b
    # Part Two: 1 loops, best of 10000 repeats: 0.00111577s
    counter = 0
    mask = 1 << pos
    for v in values:
        if v & mask == mask:
            counter += 1
        else:
            counter -= 1

    return counter >= 0


def rating(values: Tuple[int], want: bool):
    num_bits = max(values).bit_length()
    matching_values = values
    for i in reversed(range(num_bits)):
        if len(matching_values) == 1:
            break

        if most_common(matching_values, i) == want:
            matching_values = list(filter(lambda x: bit_at(x, i), matching_values))
        else:
            matching_values = list(filter(lambda x: not bit_at(x, i), matching_values))

    return matching_values[0]


def part01(data: Tuple[int]) -> int:
    gamma_rate = 0
    epsilon_rate = 0
    num_bits = max(data).bit_length()

    for i in range(num_bits):
        if most_common(data, i):
            gamma_rate |= (1 << i)
        else:
            epsilon_rate |= (1 << i)

    return gamma_rate * epsilon_rate


def part02(data: Tuple[int]) -> int:
    return rating(data, True) * rating(data, False)


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
