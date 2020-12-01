#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
from typing import List

def part01(expense_report: List[int]) -> int:
    for e in expense_report:
        partner = 2020 - e
        if partner in expense_report:
            return e * partner

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        expense_report = list(map(int, f.readlines()))
        start_time = time.perf_counter()
        print("Solution to Part 01 is:", part01(expense_report))
        part_one = time.perf_counter()
        print(f"Code took {part_one - start_time:0.8f}s to run")
