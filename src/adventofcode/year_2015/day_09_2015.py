from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

from itertools import permutations
import math


@solution_timer(2015, 9, 1)
def part_one(input_data: List[str]):
    path = {}
    locations = []
    for line in input_data:
        sLine = line.split()
        c1 = sLine[0]
        c2 = sLine[2]
        dist = sLine[4]
        path[c1 + c2] = int(dist)
        path[c2 + c1] = int(dist)
        locations.append(c1)
        locations.append(c2)

    locations = set(locations)

    shortest = math.inf
    for perm in permutations(locations):
        permDist = 0
        for c1, c2 in zip(perm[:-1], perm[1:]):
            permDist += path[c1 + c2]
        shortest = min(shortest, permDist)
    return shortest


@solution_timer(2015, 9, 2)
def part_two(input_data: List[str]):
    path = {}
    locations = []
    for line in input_data:
        sLine = line.split()
        c1 = sLine[0]
        c2 = sLine[2]
        dist = sLine[4]
        path[c1 + c2] = int(dist)
        path[c2 + c1] = int(dist)
        locations.append(c1)
        locations.append(c2)

    locations = set(locations)

    longest = -math.inf
    for perm in permutations(locations):
        permDist = 0
        for c1, c2 in zip(perm[:-1], perm[1:]):
            permDist += path[c1 + c2]
        longest = max(longest, permDist)
    return longest


if __name__ == "__main__":
    data = get_input_for_day(2015, 9)
    part_one(data)
    part_two(data)
