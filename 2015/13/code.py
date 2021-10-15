# Advent of code Year 2015 Day 13 solution
# Author = Frazzer951
# Date = October 2021

from itertools import permutations

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


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


def part1(input):
    people = dict()

    for line in input:
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


t1 = part1(
    [
        "Alice would gain 54 happiness units by sitting next to Bob.",
        "Alice would lose 79 happiness units by sitting next to Carol.",
        "Alice would lose 2 happiness units by sitting next to David.",
        "Bob would gain 83 happiness units by sitting next to Alice.",
        "Bob would lose 7 happiness units by sitting next to Carol.",
        "Bob would lose 63 happiness units by sitting next to David.",
        "Carol would lose 62 happiness units by sitting next to Alice.",
        "Carol would gain 60 happiness units by sitting next to Bob.",
        "Carol would gain 55 happiness units by sitting next to David.",
        "David would gain 46 happiness units by sitting next to Alice.",
        "David would lose 7 happiness units by sitting next to Bob.",
        "David would gain 41 happiness units by sitting next to Carol.",
    ]
)
print("Part One Test 1: " + str(t1))

p1 = part1(input)
print("Part One : " + str(p1))


def part2(input):
    people = dict()
    people["Luke"] = Person("Luke")

    for line in input:
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


p2 = part2(input)
print("Part Two : " + str(p2))