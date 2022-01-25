from collections import defaultdict
from typing import Dict
from typing import List
from typing import Set
from typing import Tuple

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def numParents(bag: str, bags: Dict[str, List[str]], visited: Set[str] = set()):
    parents = bags[bag]

    for p_bag in parents:
        visited.add(p_bag)
        numParents(p_bag, bags, visited)

    return len(visited)


@solution_timer(2020, 7, 1)
def part_one(input_data: List[str]):
    bags = defaultdict(list)

    for line in input_data:
        bag_type, content = line.split(" contain ")
        bag_type = bag_type.rsplit(maxsplit=1)[0]
        for content_line in content.split(", "):
            amount, content_type = content_line.split(maxsplit=1)
            content_type = content_type.rsplit(maxsplit=1)[0]
            bags[content_type].append(bag_type)

    return numParents("shiny gold", bags)


def count_sub_bags(bag: str, bags: Dict[str, List[Tuple[str, int]]]):
    sub_bags = bags[bag]
    count = 0
    for s_bag in sub_bags:
        count += s_bag[1]
        count += s_bag[1] * count_sub_bags(s_bag[0], bags)
    return count


@solution_timer(2020, 7, 2)
def part_two(input_data: List[str]):
    bags = defaultdict(list)

    for line in input_data:
        bag_type, content = line.split(" contain ")
        bag_type = bag_type.rsplit(maxsplit=1)[0]
        for content_line in content.split(", "):
            amount, content_type = content_line.split(maxsplit=1)
            amount = 0 if amount == "no" else int(amount)
            content_type = content_type.rsplit(maxsplit=1)[0]
            bags[bag_type].append((content_type, amount))

    return count_sub_bags("shiny gold", bags)


if __name__ == "__main__":
    data = get_input_for_day(2020, 7)
    part_one(data)
    part_two(data)
