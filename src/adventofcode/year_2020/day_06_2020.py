from typing import List
from typing import Set

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2020, 6, 1)
def part_one(input_data: List[str]):
    running_sum = 0
    cur_group = ""
    for line in input_data:
        if line == "":
            running_sum += len(set(cur_group))
            cur_group = ""
        else:
            cur_group += line
    running_sum += len(set(cur_group))
    return running_sum


@solution_timer(2020, 6, 2)
def part_two(input_data: List[str]):
    running_sum = 0
    cur_group: Set[str] = set()
    new = True
    for line in input_data:
        if line == "":
            running_sum += len(cur_group)
            cur_group = set()
            new = True
        else:
            if new:
                cur_group = set(line)
                new = False
            else:
                cur_group = cur_group.intersection(set(line))
    running_sum += len(cur_group)
    return running_sum


if __name__ == "__main__":
    data = get_input_for_day(2020, 6)
    part_one(data)
    part_two(data)
