from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

import itertools


def get_containers(input_data: List[str]) -> List[int]:
    return list(map(int, input_data))


def find_combinations(input_data: List[str], liters: int = 150) -> int:
    # Only have one container of each size, so we can get all combinations of all containers
    # with varying lengths and calculate which combination equals 150 liters
    total_combinations = 0
    containers = get_containers(input_data)

    for container in range(len(containers)):
        container_total = 0
        for combination in itertools.combinations(containers, container):
            if sum(combination) == liters:
                container_total += 1

        total_combinations += container_total

    return total_combinations


def find_different_ways(input_data: List[str], liters: int = 150) -> int:
    possible_combinations = []
    minimum_containers = 0
    containers = get_containers(input_data)

    for container in range(len(containers)):
        for combination in itertools.combinations(containers, container):
            if len(combination) > minimum_containers != 0:
                continue

            if sum(combination) == liters:
                minimum_containers = (
                    len(combination)
                    if minimum_containers == 0 or len(combination) < minimum_containers
                    else minimum_containers
                )
                possible_combinations.append(combination)

    return len(
        [
            container
            for container in possible_combinations
            if len(container) == minimum_containers
        ]
    )


@solution_timer(2015, 17, 1)
def part_one(input_data: List[str]):
    answer = find_combinations(input_data)

    if not answer:
        raise SolutionNotFoundException(2015, 17, 1)

    return answer


@solution_timer(2015, 17, 2)
def part_two(input_data: List[str]):
    answer = find_different_ways(input_data)

    if not answer:
        raise SolutionNotFoundException(2015, 17, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 17)
    part_one(data)
    part_two(data)
