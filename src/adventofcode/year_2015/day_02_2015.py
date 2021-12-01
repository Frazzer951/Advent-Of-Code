from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2015, 2, 1)
def part_one(input_data: List[str]):
    area = 0

    for line in input_data:
        sides = line.split("x")
        sides = [int(x) for x in sides]
        s1 = sides[0] * sides[1]
        s2 = sides[1] * sides[2]
        s3 = sides[2] * sides[0]
        smallest = min(s1, s2, s3)
        area += (2 * s1 + 2 * s2 + 2 * s3) + smallest

    return area


@solution_timer(2015, 2, 2)
def part_two(input_data: List[str]):
    length = 0

    for line in input_data:
        sides = line.split("x")
        sides = [int(x) for x in sides]
        sides = sorted(sides)
        length += 2 * sides[0] + 2 * sides[1] + (sides[0] * sides[1] * sides[2])

    return length


if __name__ == "__main__":
    data = get_input_for_day(2015, 2)
    part_one(data)
    part_two(data)
