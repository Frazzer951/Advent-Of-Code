from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

import hashlib


@solution_timer(2015, 4, 1)
def part_one(input_data: List[str]):
    input_data = input_data[0]
    for i in range(10000000):
        string = input_data + str(i)
        if hashlib.md5(string.encode('utf-8')).hexdigest()[:5] == "00000":
            return i
    return None


@solution_timer(2015, 4, 2)
def part_two(input_data: List[str]):
    input_data = input_data[0]
    for i in range(10000000):
        string = input_data + str(i)
        if hashlib.md5(string.encode('utf-8')).hexdigest()[:6] == "000000":
            return i
    return None


if __name__ == "__main__":
    data = get_input_for_day(2015, 4)
    part_one(data)
    part_two(data)
