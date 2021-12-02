from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2020, 1, 1)
def part_one(input_data: List[str]):
    input_data = [int(x) for x in input_data]
    for num in input_data:
        if 2020 - num in input_data:
            return num * (2020 - num)

    raise SolutionNotFoundException(2020, 1, 1)


@solution_timer(2020, 1, 2)
def part_two(input_data: List[str]):
    input_data = [int(x) for x in input_data]

    for num1 in input_data:
        for num2 in input_data:
            if 2020 - num1 - num2 in input_data:
                return num1 * num2 * (2020 - num1 - num2)

    raise SolutionNotFoundException(2020, 1, 2)


if __name__ == "__main__":
    data = get_input_for_day(2020, 1)
    part_one(data)
    part_two(data)
