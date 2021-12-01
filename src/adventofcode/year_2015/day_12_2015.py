from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

import json


def sum_of_nums(item, skipRed=False):
    if isinstance(item, list):
        return sum([sum_of_nums(i, skipRed) for i in item])
    if isinstance(item, dict):
        if skipRed and "red" in item.values():
            return 0
        return sum([sum_of_nums(i, skipRed) for i in item.values()])
    if isinstance(item, int):
        return item
    return 0


@solution_timer(2015, 12, 1)
def part_one(input_data: List[str]):
    input_data = json.loads(input_data[0])
    return sum_of_nums(input_data)


@solution_timer(2015, 12, 2)
def part_two(input_data: List[str]):
    input_data = json.loads(input_data[0])
    return sum_of_nums(input_data, True)


if __name__ == "__main__":
    data = get_input_for_day(2015, 12)
    part_one(data)
    part_two(data)
