from collections import defaultdict
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2016, 10, 1)
def part_one(input_data: List[str], c1: int = 61, c2: int = 17):
    bots = defaultdict(list)
    outputs = defaultdict(int)
    instructions = input_data
    remaining = []

    while len(instructions) > 0:
        for instruction in instructions:
            i_split = instruction.split()
            if i_split[0] == "value":
                bots[i_split[5]].append(int(i_split[1]))
            elif i_split[0] == "bot":
                if len(bots[i_split[1]]) == 2:
                    if bots[i_split[1]] == [c1, c2] or bots[i_split[1]] == [c2, c1]:
                        return int(i_split[1])
                    low = min(bots[i_split[1]])
                    high = max(bots[i_split[1]])
                    bots[i_split[1]].clear()
                    if i_split[5] == "bot":
                        bots[i_split[6]].append(low)
                    else:
                        outputs[i_split[6]] = low
                    if i_split[10] == "bot":
                        bots[i_split[11]].append(high)
                    else:
                        outputs[i_split[11]] = high
                else:
                    remaining.append(instruction)
        instructions = remaining.copy()
        remaining = []
    raise SolutionNotFoundException(2016, 10, 1)


@solution_timer(2016, 10, 2)
def part_two(input_data: List[str]):
    bots = defaultdict(list)
    outputs = defaultdict(int)
    instructions = input_data
    remaining = []

    while len(instructions) > 0:
        for instruction in instructions:
            i_split = instruction.split()
            if i_split[0] == "value":
                bots[i_split[5]].append(int(i_split[1]))
            elif i_split[0] == "bot":
                if len(bots[i_split[1]]) == 2:
                    low = min(bots[i_split[1]])
                    high = max(bots[i_split[1]])
                    bots[i_split[1]].clear()
                    if i_split[5] == "bot":
                        bots[i_split[6]].append(low)
                    else:
                        outputs[i_split[6]] = low
                    if i_split[10] == "bot":
                        bots[i_split[11]].append(high)
                    else:
                        outputs[i_split[11]] = high
                else:
                    remaining.append(instruction)
        instructions = remaining.copy()
        remaining = []
    return outputs["0"] * outputs["1"] * outputs["2"]


if __name__ == "__main__":
    data = get_input_for_day(2016, 10)
    part_one(data)
    part_two(data)
