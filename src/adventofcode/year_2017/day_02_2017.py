from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2017, 2, 1)
def part_one(input_data: List[str]):
    data = [[int(x) for x in line.split("\t")] for line in input_data]

    checksum = 0

    for line in data:
        min_value = min(line)
        max_value = max(line)
        checksum += max_value - min_value

    return checksum


@solution_timer(2017, 2, 2)
def part_two(input_data: List[str]):
    data = [[int(x) for x in line.split("\t")] for line in input_data]

    checksum = 0

    for line in data:
        for i in range(len(line)):
            for j in range(len(line)):
                if i != j and line[i] % line[j] == 0:
                    checksum += line[i] // line[j]

    return checksum


if __name__ == "__main__":
    data = get_input_for_day(2017, 2)
    part_one(data)
    part_two(data)
