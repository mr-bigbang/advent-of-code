#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import timeit
from typing import List, Optional, Tuple


class Board:
    def __init__(self, board: Tuple[int]):
        self._board = board
        self._marks = [False] * 5 * 5
        self._number = None

    def play(self, number: int) -> None:
        if number in self._board:
            i = self._board.index(number)
            self._marks[i] = True

        self._number = number

    def get_score(self) -> int:
        score = sum([self._board[i] for i in range(5*5) if not self._marks[i]])

        return score * self._number

    def bingo(self) -> bool:
        for i in range(0, len(self._marks), 5):
            if sum(self._marks[i:i+5]) == 5:
                return True

        for i in range(5):
            if sum(self._marks[i::5]) == 5:
                return True

        return False


def parse_input(values: Tuple[str]) -> Tuple[List[Board], Tuple[int]]:
    draws = tuple(map(int, values[0].split(',')))

    board_lines = map(lambda l: l.replace('\n', ' ').replace('  ', ' ').split(' '), values[1:])
    boards = [Board(tuple(map(int, filter(lambda x: x != '', b)))) for b in board_lines]

    return boards, draws


def part01(values: Tuple[str]) -> int:
    boards, draw = parse_input(values)

    for i in draw:
        # Set number on all boards
        list(map(lambda x: x.play(i), boards))

        # Check if winner
        w = list(filter(lambda x: x.bingo(), boards))
        if len(w) > 0:
            return w[0].get_score()


def part02(values: Tuple[str]) -> int:
    pass


if __name__ == '__main__':
    BENCH_LOOPS = 1
    BENCH_REPEAT = 10000

    with open("input.txt", "r") as f:
        # data[0] is the draws
        # data[1:] are the boards
        data = tuple(f.read().split('\n\n'))

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
