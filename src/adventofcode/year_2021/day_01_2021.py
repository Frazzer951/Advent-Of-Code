from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2021, 1, 1)
def part_one(input_data: List[str]):
    increasing_count = 0
    for i in range(1, len(input_data)):
        if int(input_data[i - 1]) < int(input_data[i]):
            increasing_count += 1
    return increasing_count


@solution_timer(2021, 1, 2)
def part_two(input_data: List[str]):
    input_data = [int(x) for x in input_data]
    increasing_count = 0
    for i in range(1, len(input_data) - 2):
        t1 = input_data[i - 1 : i + 2]
        t2 = input_data[i : i + 3]
        t1 = sum(t1)
        t2 = sum(t2)
        if sum(input_data[i - 1 : i + 2]) < sum(input_data[i : i + 3]):
            increasing_count += 1
    return increasing_count


if __name__ == "__main__":
    data = get_input_for_day(2021, 1)
    part_one(data)
    part_two(data)
