from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def is_valid_passphrase(passphrase: str) -> bool:
    words = passphrase.split()
    return len(words) == len(set(words))


@solution_timer(2017, 4, 1)
def part_one(input_data: List[str]):
    count = 0
    for passphrase in input_data:
        if is_valid_passphrase(passphrase):
            count += 1
    return count


def is_valid_passphrase_2(passphrase: str) -> bool:
    words = passphrase.split()
    return len(words) == len({"".join(sorted(word)) for word in words})


@solution_timer(2017, 4, 2)
def part_two(input_data: List[str]):
    count = 0
    for passphrase in input_data:
        if is_valid_passphrase_2(passphrase):
            count += 1
    return count


if __name__ == "__main__":
    data = get_input_for_day(2017, 4)
    part_one(data)
    part_two(data)
