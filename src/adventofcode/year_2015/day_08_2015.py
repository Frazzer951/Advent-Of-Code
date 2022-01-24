import re
from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def size_in_memory(str):
    assert str[0] == '"'
    assert str[-1] == '"'
    mem = str[1:-1]
    mem = mem.replace("\\\\", "x")
    mem = mem.replace('\\"', "x")
    mem, _ = re.subn("\\\\x..", "x", mem)
    return len(mem)


def size_encoded(str):
    encoded = str
    encoded = encoded.replace("\\", "\\\\")
    encoded = encoded.replace('"', '\\"')
    encoded = '"' + encoded + '"'
    return len(encoded)


@solution_timer(2015, 8, 1)
def part_one(input_data: List[str]):
    count = 0

    for line in input_data:
        line = line.strip()
        line_count = len(line)
        line_mem = size_in_memory(line)
        count += line_count - line_mem

    return count


@solution_timer(2015, 8, 2)
def part_two(input_data: List[str]):
    count = 0

    for line in input_data:
        line = line.strip()
        line_count = len(line)
        line_enc = size_encoded(line)
        count += line_enc - line_count

    return count


if __name__ == "__main__":
    data = get_input_for_day(2015, 8)
    part_one(data)
    part_two(data)
