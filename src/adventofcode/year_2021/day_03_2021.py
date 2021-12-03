from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2021, 3, 1)
def part_one(input_data: List[str]):
    bit_counts = [[0, 0] for i in range(len(input_data[0]))]

    for line in input_data:
        for i in range(len(line)):
            bit_counts[i][int(line[i])] += 1

    gamma_bits = "".join("1" if i[1] > i[0] else "0" for i in bit_counts)
    epsilon_bits = "".join("1" if i[1] < i[0] else "0" for i in bit_counts)
    gamma = int(gamma_bits, 2)
    epsilon = int(epsilon_bits, 2)

    return gamma * epsilon


def filter_bits(bits: List[str], oxygen: bool):
    i = 0
    while len(bits) > 1:
        counts = [0, 0]
        for j in range(len(bits)):
            counts[int(bits[j][i])] += 1
        mask = ""
        if oxygen:
            if counts[0] == counts[1]:
                mask = "1"
            else:
                mask = "0" if counts[0] > counts[1] else "1"
        else:
            if counts[0] == counts[1]:
                mask = "0"
            else:
                mask = "0" if counts[0] < counts[1] else "1"

        bits = [b for b in bits if b[i] == mask]
        i += 1
    if bits:
        return bits[0]
    else:
        raise SolutionNotFoundException(2021, 3, 2)


@solution_timer(2021, 3, 2)
def part_two(input_data: List[str]):
    oxygen_bits = filter_bits(input_data.copy(), True)
    c02_bits = filter_bits(input_data.copy(), False)
    oxygen = int(oxygen_bits, 2)
    c02 = int(c02_bits, 2)
    return oxygen * c02


if __name__ == "__main__":
    data = get_input_for_day(2021, 3)
    part_one(data)
    part_two(data)
