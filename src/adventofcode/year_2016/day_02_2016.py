from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def decipherCode(input_data, keypad=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], x=1, y=1):
    code = ""
    for line in input_data:
        for dir in line:
            if dir == "U":
                if y > 0 and keypad[y - 1][x] is not None:
                    y -= 1
            elif dir == "D":
                if y < len(keypad) - 1 and keypad[y + 1][x] is not None:
                    y += 1
            elif dir == "L":
                if x > 0 and keypad[y][x - 1] is not None:
                    x -= 1
            elif dir == "R":
                if x < len(keypad[0]) - 1 and keypad[y][x + 1] is not None:
                    x += 1
        code += str(keypad[y][x])
    return code


@solution_timer(2016, 2, 1)
def part_one(input_data: List[str]):
    return decipherCode(input_data)


@solution_timer(2016, 2, 2)
def part_two(input_data: List[str]):
    keypad = [
        [None, None, 1, None, None],
        [None, 2, 3, 4, None],
        [5, 6, 7, 8, 9],
        [None, "A", "B", "C", None],
        [None, None, "D", None, None],
    ]
    return decipherCode(input_data, keypad, 0, 2)


if __name__ == "__main__":
    data = get_input_for_day(2016, 2)
    part_one(data)
    part_two(data)
