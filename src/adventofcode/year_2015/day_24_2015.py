from functools import reduce
from itertools import combinations
from operator import mul
from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def splitPresents(weights, num_groups):
    group_size = sum(weights) // num_groups
    for i in range(len(weights)):
        qes = [reduce(mul, c) for c in combinations(weights, i) if sum(c) == group_size]
        if qes:
            return min(qes)


@solution_timer(2015, 24, 1)
def part_one(input_data: List[str]):
    nums = [int(i) for i in input_data]
    return splitPresents(nums, 3)


@solution_timer(2015, 24, 2)
def part_two(input_data: List[str]):
    nums = [int(i) for i in input_data]
    return splitPresents(nums, 4)


if __name__ == "__main__":
    data = get_input_for_day(2015, 24)
    part_one(data)
    part_two(data)
