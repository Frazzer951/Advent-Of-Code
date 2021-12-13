from typing import List, Set, Tuple

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

from copy import deepcopy


def increment_levels(levels: List[List[int]], row: int, col: int, updated: Set[Tuple[int, int]]):
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if r == row and c == col:
                continue
            if r >= 0 and r < len(levels) and c >= 0 and c < len(levels[r]):
                levels[r][c] += 1
                if levels[r][c] > 9 and (r, c) not in updated:
                    updated.add((r, c))
                    increment_levels(levels, r, c, updated)


def next_step(energy_levels: List[List[int]]):
    new_levels = deepcopy(energy_levels)
    flashes = 0
    updated = set()
    for row in range(len(energy_levels)):
        for col in range(len(energy_levels[row])):
            new_levels[row][col] = new_levels[row][col] + 1
            if new_levels[row][col] > 9 and (row, col) not in updated:
                updated.add((row, col))
                increment_levels(new_levels, row, col, updated)

    for row in range(len(energy_levels)):
        for col in range(len(energy_levels[row])):
            if new_levels[row][col] > 9:
                flashes += 1
                new_levels[row][col] = 0
    return (new_levels, flashes)


@solution_timer(2021, 11, 1)
def part_one(input_data: List[str]):
    energy_levels = [[int(x) for x in line] for line in input_data]
    flash_count = 0
    for _ in range(100):
        energy_levels, flashes = next_step(energy_levels)
        flash_count += flashes
    return flash_count


@solution_timer(2021, 11, 2)
def part_two(input_data: List[str]):
    energy_levels = [[int(x) for x in line] for line in input_data]
    flash_count = 0
    required_flashes = len(input_data) * len(input_data[0])
    iterations = 0
    while flash_count != required_flashes:
        energy_levels, flash_count = next_step(energy_levels)
        iterations += 1
    return iterations


if __name__ == "__main__":
    data = get_input_for_day(2021, 11)
    part_one(data)
    part_two(data)
