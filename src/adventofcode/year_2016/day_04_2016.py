from typing import List
import typing

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

from collections import Counter


def is_real(code):
    name = code.rsplit("-", 1)[0].replace("-", "")
    # id = code.rsplit("-", 1)[1].split("[", 1)[0]
    checksum = code.split("[")[-1].strip("]")
    checksum = list(checksum)

    letters: typing.Counter[str] = Counter(name)
    most_common = sorted(letters.most_common(), key=lambda x: (-x[1], x[0]))
    most_common = [x[0] for x in most_common]
    most_common = most_common[:5]

    if most_common != checksum:
        return False
    return True


def decrypt_name(code):
    name = code.rsplit("-", 1)[0]
    id = int(code.split("-")[-1].split("[")[0])
    new_name = ""
    for letter in name:
        if letter == "-":
            new_name += " "
        else:
            char = ord(letter) - 97
            new_char = (char + id) % 26
            new_char += 97
            new_name += chr(new_char)
    return new_name


@solution_timer(2016, 4, 1)
def part_one(input_data: List[str]):
    id_sum = 0
    for code in input_data:
        if is_real(code):
            id_sum += int(code.split("-")[-1].split("[")[0])
    return id_sum


@solution_timer(2016, 4, 2)
def part_two(input_data: List[str]):
    for code in input_data:
        if is_real(code):
            name = decrypt_name(code)
            if name == "northpole object storage":
                return int(code.split("-")[-1].split("[")[0])

    raise SolutionNotFoundException(2016, 4, 2)


if __name__ == "__main__":
    data = get_input_for_day(2016, 4)
    part_one(data)
    part_two(data)
