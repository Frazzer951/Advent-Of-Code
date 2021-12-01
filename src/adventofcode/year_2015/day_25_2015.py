from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def getCode(x, y):
    pos = (x + y - 2) * (x + y - 1) // 2 + y - 1

    val = 20151125

    for i in range(pos):
        val = val * 252533 % 33554393

    return val


@solution_timer(2015, 25, 1)
def part_one(input_data: List[str]):
    input_data = input_data[0].split()
    x = int(input_data[-3].strip(","))
    y = int(input_data[-1].strip("."))
    return getCode(x, y)


@solution_timer(2015, 25, 2)
def part_two(input_data: List[str]):
    return "2015 Finished"


if __name__ == "__main__":
    data = get_input_for_day(2015, 25)
    part_one(data)
    part_two(data)
