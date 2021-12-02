from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def is_valid_password_1(password: str) -> bool:
    rule, password = password.split(": ")
    range, letter = rule.split(" ")
    lower, upper = range.split("-")
    lower, upper = int(lower), int(upper)
    if lower <= password.count(letter) <= upper:
        return True
    return False


def is_valid_password_2(password: str) -> bool:
    rule, password = password.split(": ")
    range, letter = rule.split(" ")
    index_1, index_2 = range.split("-")
    index_1, index_2 = int(index_1), int(index_2)
    if (password[index_1 - 1] == letter and password[index_2 - 1] != letter) or (
        password[index_1 - 1] != letter and password[index_2 - 1] == letter
    ):
        return True
    return False


@solution_timer(2020, 2, 1)
def part_one(input_data: List[str]):
    count = 0
    for password in input_data:
        if is_valid_password_1(password):
            count += 1
    return count


@solution_timer(2020, 2, 2)
def part_two(input_data: List[str]):
    count = 0
    for password in input_data:
        if is_valid_password_2(password):
            count += 1
    return count


if __name__ == "__main__":
    data = get_input_for_day(2020, 2)
    part_one(data)
    part_two(data)
