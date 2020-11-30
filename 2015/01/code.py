#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# find_floor
def part01(directions: str):
    floor = 0
    for c in directions:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        else:
            pass
    return floor

# find_position
def part02(directions: str):
    position = 1
    floor = 0
    for c in directions:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        else:
            pass

        if floor < 0:
            return position
        else:
            position += 1

    return position

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        instructions = f.read()
        floor = part01(instructions)
        print("Santa is on floor:", floor)
        position = part02(instructions)
        print("Santa enters the basement in position", position)
