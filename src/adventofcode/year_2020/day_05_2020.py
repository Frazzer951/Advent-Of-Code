from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def get_seat_from_code(seat_code: str):
    row_lower = 0
    row_upper = 127
    column_lower = 0
    column_upper = 7
    row_code = seat_code[:7]
    col_code = seat_code[7:]

    for c in row_code:
        if c == "F":
            row_upper = (row_upper + row_lower) // 2
        else:
            row_lower = (row_upper + row_lower) // 2 + 1
    for c in col_code:
        if c == "L":
            column_upper = (column_upper + column_lower) // 2
        else:
            column_lower = (column_upper + column_lower) // 2 + 1

    return row_lower * 8 + column_lower


@solution_timer(2020, 5, 1)
def part_one(input_data: List[str]):
    highest_seat_code = 0
    for code in input_data:
        seat_code = get_seat_from_code(code)
        if seat_code > highest_seat_code:
            highest_seat_code = seat_code
    return highest_seat_code


@solution_timer(2020, 5, 2)
def part_two(input_data: List[str]):
    codes = []
    for code in input_data:
        codes.append(get_seat_from_code(code))
    codes.sort()
    for i in range(len(codes) - 1):
        if codes[i + 1] - codes[i] == 2:
            return codes[i] + 1
    raise SolutionNotFoundException(2020, 5, 2)


if __name__ == "__main__":
    data = get_input_for_day(2020, 5)
    part_one(data)
    part_two(data)
