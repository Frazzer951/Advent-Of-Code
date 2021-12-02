from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def check_slope(x: int, y: int, map: List[str]):
    trees_hit = 0
    pos = (0, 0)
    width = len(map[0])
    height = len(map)
    while pos[1] < height:
        if map[pos[1]][pos[0] % width] == "#":
            trees_hit += 1
        pos = ((pos[0] + x) % width, pos[1] + y)
    return trees_hit


@solution_timer(2020, 3, 1)
def part_one(input_data: List[str]):
    return check_slope(3, 1, input_data)


@solution_timer(2020, 3, 2)
def part_two(input_data: List[str]):
    return (
        check_slope(1, 1, input_data)
        * check_slope(3, 1, input_data)
        * check_slope(5, 1, input_data)
        * check_slope(7, 1, input_data)
        * check_slope(1, 2, input_data)
    )


if __name__ == "__main__":
    data = get_input_for_day(2020, 3)
    part_one(data)
    part_two(data)
