from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

import math


def calculate_fuel_cost(heights: List[int], position: int):
    cost = 0
    for height in heights:
        cost += abs(height - position)
    return cost


def calculate_fuel_cost_2(heights: List[int], position: int):
    cost = 0
    for height in heights:
        diff = abs(height - position)
        cost += math.floor(diff * (diff + 1) / 2)
    return cost


@solution_timer(2021, 7, 1)
def part_one(input_data: List[str]):
    input_data = [int(x) for x in input_data[0].split(",")]
    min_val = min(input_data)
    max_val = max(input_data)

    min_cost = math.inf

    for i in range(min_val, max_val + 1):
        cost = calculate_fuel_cost(input_data, i)
        if cost < min_cost:
            min_cost = cost

    return min_cost


@solution_timer(2021, 7, 2)
def part_two(input_data: List[str]):
    input_data = [int(x) for x in input_data[0].split(",")]
    min_val = min(input_data)
    max_val = max(input_data)

    min_cost = math.inf

    for i in range(min_val, max_val + 1):
        cost = calculate_fuel_cost_2(input_data, i)
        if cost < min_cost:
            min_cost = cost

    return min_cost


if __name__ == "__main__":
    data = get_input_for_day(2021, 7)
    part_one(data)
    part_two(data)
