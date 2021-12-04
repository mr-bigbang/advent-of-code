#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import timeit
from typing import List, Optional, Tuple, Union


class Board:
    # Board-Layout
    # [ [ (int, bool), (int, bool), (int, bool), (int, bool), (int, bool)],
    #   [ (int, bool), (int, bool), (int, bool), (int, bool), (int, bool)],
    #   [ (int, bool), (int, bool), (int, bool), (int, bool), (int, bool)],
    #   [ (int, bool), (int, bool), (int, bool), (int, bool), (int, bool)],
    #   [ (int, bool), (int, bool), (int, bool), (int, bool), (int, bool)] ]

    def __init__(self):
        self._board = []
        self._number = None

    def add_row(self, row: Tuple[int]) -> None:
        self._board.append(list(map(list, zip(row, [False] * 5))))

    def bingo(self, number: int) -> None:
        for r in range(5):
            for c in range(5):
                if self._board[r][c][0] == number:
                    self._board[r][c][1] = True
                    break

        self._number = number

    def get_score(self) -> int:
        score = 0
        for r in self._board:
            for c in r:
                if not c[1]:
                    score += c[0]

        return score * self._number

    def is_winner(self) -> bool:
        # Check rows
        for r in self._board:
            if len(list(filter(lambda x: x[1], r))) == 5:
                return True

        # Check columns
        for c in range(5):
            if len(list(filter(lambda x: x[1], [row[c] for row in self._board]))) == 5:
                return True

        return False


def parse_input(values: Tuple[str]) -> Tuple[List[Board], Tuple[int]]:
    draws = tuple(map(int, values[0].split(',')))
    boards = []

    board = Board()
    for line in values[2:]:
        if line and line != '\n':
            board.add_row(tuple(map(int, line.replace("  ", " ").strip().split(" "))))
        else:
            boards.append(board)
            board = Board()

    return boards, draws


def part01(values: Tuple[str]) -> int:
    boards, draw = parse_input(values)

    winner: Board = None
    for i in draw:
        # Set number on all boards
        list(map(lambda x: x.bingo(i), boards))

        # Check if winner
        w = list(filter(lambda x: x.is_winner(), boards))
        if len(w) > 0:
            winner = w[0]
            break

    return winner.get_score()


def part02(values: Tuple[str]) -> int:
    pass


if __name__ == '__main__':
    BENCH_LOOPS = 1
    BENCH_REPEAT = 10000

    with open("input.txt", "r") as f:
        #data = list(map(int, f.readlines()))
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
