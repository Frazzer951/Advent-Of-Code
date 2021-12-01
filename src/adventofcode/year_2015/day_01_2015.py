from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2015, 1, 1)
def part_one(input_data: List[str]):
    floor = 0

    for c in input_data[0]:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1

    return floor


@solution_timer(2015, 1, 2)
def part_two(input_data: List[str]):
    floor = 0

    for i in range(len(input_data[0])):
        if input_data[0][i] == "(":
            floor += 1
        if input_data[0][i] == ")":
            floor -= 1
        if floor == -1:
            return i + 1

    raise SolutionNotFoundException(2015, 1, 2)


if __name__ == "__main__":
    data = get_input_for_day(2015, 1)
    part_one(data)
    part_two(data)
