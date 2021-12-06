from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2021, 6, 1)
def part_one(input_data: List[str]):
    fish = [int(x) for x in input_data[0].split(",")]

    for _ in range(80):
        new_fish = []
        for i in range(len(fish)):
            if fish[i] - 1 < 0:
                new_fish.append(8)
                new_fish.append(6)
            else:
                new_fish.append(fish[i] - 1)
        fish = new_fish

    return len(fish)


@solution_timer(2021, 6, 2)
def part_two(input_data: List[str]):
    fish_ages = [int(x) for x in input_data[0].split(",")]

    fish_by_age = [0] * 9

    for fish in fish_ages:
        fish_by_age[fish] += 1

    for _ in range(256):
        new_fish = [0] * 9

        for i in range(len(fish_by_age)):
            if i == 0:
                new_fish[6] = fish_by_age[i]
                new_fish[8] = fish_by_age[i]
            else:
                new_fish[i - 1] += fish_by_age[i]
        fish_by_age = new_fish

    return sum(fish_by_age)


if __name__ == "__main__":
    data = get_input_for_day(2021, 6)
    part_one(data)
    part_two(data)
