from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def rotate(dir, turn):
    if turn == "R":
        if dir == "n":
            return "e"
        elif dir == "e":
            return "s"
        elif dir == "s":
            return "w"
        elif dir == "w":
            return "n"
    elif turn == "L":
        if dir == "n":
            return "w"
        elif dir == "e":
            return "n"
        elif dir == "s":
            return "e"
        elif dir == "w":
            return "s"


def numBlocksAway_1(moves):
    x = 0
    y = 0
    dir = "n"
    for move in moves:
        if move[0] == "R":
            dir = rotate(dir, "R")
        elif move[0] == "L":
            dir = rotate(dir, "L")

        amount = int(move[1:])
        if dir == "n":
            y += amount
        elif dir == "e":
            x += amount
        elif dir == "s":
            y -= amount
        elif dir == "w":
            x -= amount
    return abs(x) + abs(y)


def numBlocksAway_2(moves):
    locations = []
    x = 0
    y = 0
    dir = "n"
    for move in moves:
        if move[0] == "R":
            dir = rotate(dir, "R")
        elif move[0] == "L":
            dir = rotate(dir, "L")

        amount = int(move[1:])
        if dir == "n":
            for i in range(y, y + amount):
                if (x, i) in locations:
                    return abs(x) + abs(i)
                else:
                    locations.append((x, i))
            y += amount
        elif dir == "e":
            for i in range(x, x + amount):
                if (i, y) in locations:
                    return abs(i) + abs(y)
                else:
                    locations.append((i, y))
            x += amount
        elif dir == "s":
            for i in range(y, y - amount, -1):
                if (x, i) in locations:
                    return abs(x) + abs(i)
                else:
                    locations.append((x, i))
            y -= amount
        elif dir == "w":
            for i in range(x, x - amount, -1):
                if (i, y) in locations:
                    return abs(i) + abs(y)
                else:
                    locations.append((i, y))
            x -= amount
    return abs(x) + abs(y)


@solution_timer(2016, 1, 1)
def part_one(input_data: List[str]):
    input_data = [x.strip(",") for x in input_data[0].split()]
    return numBlocksAway_1(input_data)


@solution_timer(2016, 1, 2)
def part_two(input_data: List[str]):
    input_data = [x.strip(",") for x in input_data[0].split()]
    return numBlocksAway_2(input_data)


if __name__ == "__main__":
    data = get_input_for_day(2016, 1)
    part_one(data)
    part_two(data)
