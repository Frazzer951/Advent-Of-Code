from dataclasses import dataclass
from posixpath import split
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2020, 8, 1)
def part_one(input_data: List[str]):
    acc = 0
    ip = 0
    visited = set()
    while ip < len(input_data):
        if ip in visited:
            return acc
        visited.add(ip)
        cmd_split = input_data[ip].split()
        if cmd_split[0] == "acc":
            acc += int(cmd_split[1])
            ip += 1
        elif cmd_split[0] == "jmp":
            ip += int(cmd_split[1])
        elif cmd_split[0] == "nop":
            ip += 1
        else:
            raise SolutionNotFoundException(2020, 8, 1)
    raise SolutionNotFoundException(2020, 8, 1)


@dataclass
class Command:
    cmd: str
    arg: int


def run_code(code: List[Command]):
    acc = 0
    ip = 0
    visited = set()
    while ip < len(code):
        if ip in visited:
            return -1
        visited.add(ip)
        cmd = code[ip]
        if cmd.cmd == "acc":
            acc += cmd.arg
            ip += 1
        elif cmd.cmd == "jmp":
            ip += cmd.arg
        elif cmd.cmd == "nop":
            ip += 1
        else:
            raise SolutionNotFoundException(2020, 8, 2)
    return acc


@solution_timer(2020, 8, 2)
def part_two(input_data: List[str]):
    code = []
    jmp_nop_locs = []

    for i, line in enumerate(input_data):
        cmd, arg = line.split()
        arg = int(arg)
        if any(cmd == x for x in ["jmp", "nop"]):
            jmp_nop_locs.append(i)
        code.append(Command(cmd, arg))

    for loc in jmp_nop_locs:
        if code[loc].cmd == "jmp":
            code[loc].cmd = "nop"
            result = run_code(code)
            if result != -1:
                return result
            code[loc].cmd = "jmp"
        elif code[loc].cmd == "nop":
            code[loc].cmd = "jmp"
            result = run_code(code)
            if result != -1:
                return result
            code[loc].cmd = "nop"
        else:
            raise SolutionNotFoundException(2020, 8, 2)

    raise SolutionNotFoundException(2020, 8, 2)


if __name__ == "__main__":
    data = get_input_for_day(2020, 8)
    part_one(data)
    part_two(data)
