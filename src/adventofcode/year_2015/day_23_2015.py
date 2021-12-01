from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def sim_code(input, registers=None):
    if registers is None:
        registers = {"a": 0, "b": 0}

    ip = 0
    while ip < len(input):
        line = input[ip].split()
        if line[0] == "hlf":
            reg = line[1]
            registers[reg] = registers[reg] // 2
        elif line[0] == "tpl":
            reg = line[1]
            registers[reg] = registers[reg] * 3
        elif line[0] == "inc":
            reg = line[1]
            registers[reg] += 1
        elif line[0] == "jmp":
            ip += int(line[1])
            continue
        elif line[0] == "jie":
            reg = line[1].strip(",")
            if registers[reg] % 2 == 0:
                ip += int(line[2])
                continue
        elif line[0] == "jio":
            reg = line[1].strip(",")
            if registers[reg] == 1:
                ip += int(line[2])
                continue
        ip += 1
    return registers


@solution_timer(2015, 23, 1)
def part_one(input_data: List[str]):
    return sim_code(input_data)["b"]


@solution_timer(2015, 23, 2)
def part_two(input_data: List[str]):
    return sim_code(input_data, {"a": 1, "b": 0})["b"]


if __name__ == "__main__":
    data = get_input_for_day(2015, 23)
    part_one(data)
    part_two(data)
