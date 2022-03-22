from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2017, 1, 1)
def part_one(input_data: List[str]):
    data = [int(x) for x in input_data[0]]

    sum = 0

    for i in range(len(data)):
        if data[i] == data[(i + 1) % len(data)]:
            sum += data[i]

    return sum


@solution_timer(2017, 1, 2)
def part_two(input_data: List[str]):
    data = [int(x) for x in input_data[0]]

    sum = 0
    steps = len(data) // 2

    for i in range(len(data)):
        if data[i] == data[(i + steps) % len(data)]:
            sum += data[i]

    return sum


if __name__ == "__main__":
    data = get_input_for_day(2017, 1)
    part_one(data)
    part_two(data)
