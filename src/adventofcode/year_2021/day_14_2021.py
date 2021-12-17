from typing import List, Dict

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

from collections import Counter
from more_itertools import windowed


@solution_timer(2021, 14, 1)
def part_one(input_data: List[str]):
    polymer = input_data[0]
    input_data = input_data[2:]
    insertions = {}
    for line in input_data:
        code, insert = line.strip().split(" -> ")
        insertions[code] = insert

    for _ in range(10):
        i = 0
        while i < len(polymer) - 1:
            insert = insertions[polymer[i: i + 2]]
            polymer = polymer[: i + 1] + insert + polymer[i + 1:]
            i += 2
    counts = Counter(polymer)
    mostCom = counts.most_common()[0]
    leastCom = counts.most_common()[-1]
    return mostCom[1] - leastCom[1]


def insert_elements_smart(pair_count: Dict[str, int], element_count: Dict[str, int], rules: Dict[str, str]):
    new_pair_count = pair_count.copy()
    for key in pair_count:
        pair = list(key)
        insert_element = rules[key]
        element_count[insert_element] += pair_count[key]
        new_pair_count["".join([pair[0], insert_element])] += pair_count[key]
        new_pair_count["".join([insert_element, pair[1]])] += pair_count[key]
        new_pair_count[key] -= pair_count[key]
    return new_pair_count, element_count


@solution_timer(2021, 14, 2)
def part_two(input_data: List[str]):
    polymer: str = input_data[0]
    input_data = input_data[2:]
    insertions = {}
    for line in input_data:
        code, insert = line.strip().split(" -> ")
        insertions[code] = insert

    element_count = Counter(polymer)
    pair_count = Counter(dict.fromkeys(insertions.keys(), 0))
    for pair in windowed(polymer, 2):
        pair_count["".join(pair)] += 1  # type: ignore
    for i in range(40):
        pair_count, element_count = insert_elements_smart(pair_count, element_count, insertions)
    return max(element_count.values()) - min(element_count.values())


if __name__ == "__main__":
    data = get_input_for_day(2021, 14)
    part_one(data)
    part_two(data)
