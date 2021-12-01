from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2015, 3, 1)
def part_one(input_data: List[str]):
    x, y = 0, 0
    visited = set()
    visited.add((x, y))

    for dir in input_data[0]:
        if dir == "^":
            y += 1
        if dir == ">":
            x += 1
        if dir == "v":
            y -= 1
        if dir == "<":
            x -= 1
        visited.add((x, y))
    return len(visited)


@solution_timer(2015, 3, 2)
def part_two(input_data: List[str]):
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    visited = set()
    visited.add((x1, y1))
    visited.add((x2, y2))

    santa = True

    for dir in input_data[0]:
        if dir == "^":
            if santa:
                y1 += 1
            else:
                y2 += 1
        if dir == ">":
            if santa:
                x1 += 1
            else:
                x2 += 1
        if dir == "v":
            if santa:
                y1 -= 1
            else:
                y2 -= 1
        if dir == "<":
            if santa:
                x1 -= 1
            else:
                x2 -= 1
        if santa:
            visited.add((x1, y1))
        else:
            visited.add((x2, y2))
        santa = not santa
    return len(visited)


if __name__ == "__main__":
    data = get_input_for_day(2015, 3)
    part_one(data)
    part_two(data)
