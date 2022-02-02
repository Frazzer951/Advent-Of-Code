from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2020, 10, 1)
def part_one(input_data: List[str]):
    adapters = [int(x) for x in input_data]
    adapters.sort()

    differences = {
        0: 0,
        1: 0,
        2: 0,
        3: 1,
    }

    for i in range(len(adapters)):
        if i == 0:
            differences[adapters[i] - 0] += 1
        else:
            differences[adapters[i] - adapters[i - 1]] += 1

    return differences[1] * differences[3]


@solution_timer(2020, 10, 2)
def part_two(input_data: List[str]):
    adapters = [int(x) for x in input_data]
    adapters.append(max(adapters) + 3)
    adapters.sort()
    counter = {0: 1}
    for adapter in adapters:
        counter[adapter] = counter.get(adapter - 3, 0) + counter.get(adapter - 2, 0) + counter.get(adapter - 1, 0)
    return counter[adapters[-1]]


if __name__ == "__main__":
    data = get_input_for_day(2020, 10)
    part_one(data)
    part_two(data)
