from typing import Dict
from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2021, 8, 1)
def part_one(input_data: List[str]):
    count = 0
    outputs = [s.split("|")[-1].strip() for s in input_data]
    for output in outputs:
        nums = output.split()
        for num in nums:
            if len(num) in [2, 3, 4, 7]:
                count += 1
    return count


def get_mapping(patterns):
    pattern_of_1 = pattern_of_4 = None
    mapping: Dict[str, int] = {}

    for pattern in patterns:
        sorted_pattern_str = "".join(sorted(pattern))
        pattern = set(pattern)

        if len(pattern) == 2:
            pattern_of_1 = pattern
            mapping[sorted_pattern_str] = 1
            # print(1, sorted_pattern_str)
        elif len(pattern) == 3:
            mapping[sorted_pattern_str] = 7
            # print(7, sorted_pattern_str)
        elif len(pattern) == 4:
            pattern_of_4 = pattern
            mapping[sorted_pattern_str] = 4
            # print(4, sorted_pattern_str)
        elif len(pattern) == 7:
            mapping[sorted_pattern_str] = 8
            # print(8, sorted_pattern_str)

    for pattern in patterns:
        sorted_pattern_str = "".join(sorted(pattern))
        if sorted_pattern_str in mapping:
            continue
        pattern = set(pattern)

        if len(pattern) == 6:
            if len(pattern & pattern_of_1) == 2:
                if len(pattern & pattern_of_4) == 3:
                    mapping[sorted_pattern_str] = 0
                    # print(0, sorted_pattern_str)
                else:
                    mapping[sorted_pattern_str] = 9
                    # print(9, sorted_pattern_str)
            else:
                mapping[sorted_pattern_str] = 6
                # print(6, sorted_pattern_str)
        elif len(pattern) == 5:
            if len(pattern & pattern_of_1) == 1:
                if len(pattern & pattern_of_4) == 2:
                    mapping[sorted_pattern_str] = 2
                    # print(2, sorted_pattern_str)
                else:
                    mapping[sorted_pattern_str] = 5
                    # print(5, sorted_pattern_str)
            else:
                mapping[sorted_pattern_str] = 3
                # print(3, sorted_pattern_str)

    return mapping


def get_decoded_output(outputs, mapping):
    res = []

    for output in outputs:
        sorted_output = "".join(sorted(output))
        res.append(str(mapping[sorted_output]))

    return "".join(res)


@solution_timer(2021, 8, 2)
def part_two(input_data: List[str]):
    count = 0
    for line in input_data:
        patterns, digits = list(map(lambda x: x.strip().split(" "), line.split("|")))
        mapping = get_mapping(patterns)
        count += int(get_decoded_output(digits, mapping))
    return count


if __name__ == "__main__":
    data = get_input_for_day(2021, 8)
    part_one(data)
    part_two(data)
