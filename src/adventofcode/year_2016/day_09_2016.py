from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2016, 9, 1)
def part_one(input_data: List[str]):
    input_data = input_data[0]
    decompressed = ""
    i = 0
    while i < len(input_data):
        if input_data[i] == "(":
            marker_close = input_data.find(")", i)
            marker = input_data[i + 1 : marker_close]
            marker = marker.split("x")
            length = int(marker[0])
            repeat = int(marker[1])
            decompressed += input_data[marker_close + 1 : marker_close + 1 + length] * repeat
            i = marker_close + length + 1
        else:
            decompressed += input_data[i]
            i += 1
    return len(decompressed)


def part_two_helper(input_data: str):
    if "(" not in input_data:
        return len(input_data)
    ret = 0
    while "(" in input_data:
        ret += input_data.find("(")
        input_data = input_data[input_data.find("(") :]
        marker = input_data[1 : input_data.find(")")].split("x")
        input_data = input_data[input_data.find(")") + 1 :]
        ret += part_two_helper(input_data[: int(marker[0])]) * int(marker[1])
        input_data = input_data[int(marker[0]) :]
    ret += len(input_data)
    return ret


@solution_timer(2016, 9, 2)
def part_two(input_data: List[str]):
    input_data = input_data[0]
    return part_two_helper(input_data)


if __name__ == "__main__":
    data = get_input_for_day(2016, 9)
    part_one(data)
    part_two(data)
