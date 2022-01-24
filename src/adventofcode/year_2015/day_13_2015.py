from itertools import permutations
from typing import Dict
from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


class Person:
    def __init__(self, name):
        self.relation = {}
        self.name = name

    def add_relation(self, person, score):
        self.relation[person] = score


def get_happiness(person1, person2):
    hap1 = person1.relation.get(person2.name, 0)
    hap2 = person2.relation.get(person1.name, 0)
    return hap1 + hap2


@solution_timer(2015, 13, 1)
def part_one(input_data: List[str]):
    people: Dict[str, Person] = dict()

    for line in input_data:
        split_line = line.split()
        if split_line[2] == "gain":
            if split_line[0] not in people.keys():
                people[split_line[0]] = Person(split_line[0])
            people[split_line[0]].add_relation(split_line[-1][:-1], int(split_line[3]))
        elif split_line[2] == "lose":
            if split_line[0] not in people.keys():
                people[split_line[0]] = Person(split_line[0])
            people[split_line[0]].add_relation(split_line[-1][:-1], -int(split_line[3]))

    names = list(people.keys())
    overall_happiness = 0

    for perm in permutations(names):
        if perm[0] != names[0]:
            break
        happiness = 0
        for p1, p2 in zip(perm[-1:] + perm[:-1], perm[:1] + perm[1:]):
            happiness += get_happiness(people[p1], people[p2])
        overall_happiness = max(overall_happiness, happiness)
    return overall_happiness


@solution_timer(2015, 13, 2)
def part_two(input_data: List[str]):
    people = dict()
    people["Luke"] = Person("Luke")

    for line in input_data:
        split_line = line.split()
        if split_line[2] == "gain":
            if split_line[0] not in people.keys():
                people[split_line[0]] = Person(split_line[0])
            people[split_line[0]].add_relation(split_line[-1][:-1], int(split_line[3]))
        elif split_line[2] == "lose":
            if split_line[0] not in people.keys():
                people[split_line[0]] = Person(split_line[0])
            people[split_line[0]].add_relation(split_line[-1][:-1], -int(split_line[3]))

    names = list(people.keys())
    overall_happiness = 0

    for perm in permutations(names):
        if perm[0] != names[0]:
            break
        happiness = 0
        for p1, p2 in zip(perm[-1:] + perm[:-1], perm[:1] + perm[1:]):
            happiness += get_happiness(people[p1], people[p2])
        overall_happiness = max(overall_happiness, happiness)
    return overall_happiness


if __name__ == "__main__":
    data = get_input_for_day(2015, 13)
    part_one(data)
    part_two(data)
