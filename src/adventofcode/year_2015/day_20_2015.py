from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def firstHouseOverNum(n):
    house = [0] * int(n / 10)
    for i in range(1, int(n / 10)):
        for j in range(i, int(n / 10), i):
            house[j] += i * 10
    for i in range(len(house)):
        if house[i] >= n:
            return i


def firstHouseOverNum2(n):
    house = [0] * int(n / 10)
    for i in range(1, int(n / 10)):
        for j in range(i, min(int(n / 10), 50 * i), i):
            house[j] += i * 11
    for i in range(len(house)):
        if house[i] >= n:
            return i


@solution_timer(2015, 20, 1)
def part_one(input_data: List[str]):
    return firstHouseOverNum(33100000)


@solution_timer(2015, 20, 2)
def part_two(input_data: List[str]):
    return firstHouseOverNum2(33100000)


if __name__ == "__main__":
    data = get_input_for_day(2015, 20)
    part_one(data)
    part_two(data)
