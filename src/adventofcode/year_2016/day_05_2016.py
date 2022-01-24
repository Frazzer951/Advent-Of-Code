import hashlib
from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2016, 5, 1)
def part_one(input_data: List[str]):
    input_data = input_data[0]
    counter = 0
    code = ""
    while len(code) < 8:
        result = hashlib.md5(input_data.encode() + str(counter).encode())
        if result.hexdigest()[:5] == "00000":
            code += result.hexdigest()[5]
            # print(code)
        counter += 1
    return code


@solution_timer(2016, 5, 2)
def part_two(input_data: List[str]):
    input_data = input_data[0]
    counter = 0
    code = ["_"] * 8
    while "_" in code:
        result = hashlib.md5(input_data.encode() + str(counter).encode())
        if result.hexdigest()[:5] == "00000":
            pos = result.hexdigest()[5]
            if pos in "01234567" and code[int(pos)] == "_":
                code[int(pos)] = result.hexdigest()[6]
                # print("".join(code))
        counter += 1
    return "".join(code)


if __name__ == "__main__":
    data = get_input_for_day(2016, 5)
    part_one(data)
    part_two(data)
