import typing
from collections import Counter
from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def decodeMessage(input_data, part2=False):
    counters: List[typing.Counter[str]] = [Counter() for _ in range(len(input_data[0]))]
    for row in input_data:
        for i, char in enumerate(row):
            counters[i][char] += 1
    if not part2:
        message = [x.most_common(1)[0][0] for x in counters]
    else:
        message = [x.most_common()[-1][0] for x in counters]
    return "".join(message)


@solution_timer(2016, 6, 1)
def part_one(input_data: List[str]):
    return decodeMessage(input_data)


@solution_timer(2016, 6, 2)
def part_two(input_data: List[str]):
    return decodeMessage(input_data, True)


if __name__ == "__main__":
    data = get_input_for_day(2016, 6)
    part_one(data)
    part_two(data)
