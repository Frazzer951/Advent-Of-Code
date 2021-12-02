from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2021, 2, 1)
def part_one(input_data: List[str]):
    pos = 0
    depth = 0
    for command_str in input_data:
        command = command_str.split()
        if command[0] == "forward":
            pos += int(command[1])
        elif command[0] == "up":
            depth -= int(command[1])
        elif command[0] == "down":
            depth += int(command[1])
        else:
            raise SolutionNotFoundException(2021, 2, 1)
    return pos * depth


@solution_timer(2021, 2, 2)
def part_two(input_data: List[str]):
    pos = 0
    depth = 0
    aim = 0
    for command_str in input_data:
        command = command_str.split()
        if command[0] == "forward":
            pos += int(command[1])
            depth += int(command[1]) * aim
        elif command[0] == "up":
            aim -= int(command[1])
        elif command[0] == "down":
            aim += int(command[1])
        else:
            raise SolutionNotFoundException(2021, 2, 1)
    return pos * depth


if __name__ == "__main__":
    data = get_input_for_day(2021, 2)
    part_one(data)
    part_two(data)
