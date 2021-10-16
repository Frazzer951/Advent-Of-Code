# Advent of code Year 2015 Day 16 solution
# Author = Frazzer951
# Date = October 2021

from dataclasses import dataclass

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


@dataclass
class Sue:
    number: int
    children: int
    cats: int
    samoyeds: int
    pomeranians: int
    akitas: int
    vizslas: int
    goldfish: int
    trees: int
    cars: int
    perfumes: int


def part1(input):
    sues = {}
    for line in input:
        split = line.split()
        # print(split)
        number = int(split[1][:-1])
        split = split[2:]
        sues[number] = {}
        for i in range(0, len(split), 2):
            # print(split[i], split[i + 1].strip(","))
            sues[number][split[i][:-1]] = int(split[i + 1].strip(","))
    for num in sues:
        sue = sues[num]
        # print(num, sue)

        children = sue.get("children", -1)
        cats = sue.get("cats", -1)
        samoyeds = sue.get("samoyeds", -1)
        pomeranians = sue.get("pomeranians", -1)
        akitas = sue.get("akitas", -1)
        vizslas = sue.get("vizslas", -1)
        goldfish = sue.get("goldfish", -1)
        trees = sue.get("trees", -1)
        cars = sue.get("cars", -1)
        perfumes = sue.get("perfumes", -1)

        if children != 3 and children != -1:
            continue
        if cats != 7 and cats != -1:
            continue
        if samoyeds != 2 and samoyeds != -1:
            continue
        if pomeranians != 3 and pomeranians != -1:
            continue
        if akitas != 0 and akitas != -1:
            continue
        if vizslas != 0 and vizslas != -1:
            continue
        if goldfish != 5 and goldfish != -1:
            continue
        if trees != 3 and trees != -1:
            continue
        if cars != 2 and cars != -1:
            continue
        if perfumes != 1 and perfumes != -1:
            continue
        return num


p1 = part1(input)
print("Part One : " + str(p1))


def part2(input):
    sues = {}
    for line in input:
        split = line.split()
        # print(split)
        number = int(split[1][:-1])
        split = split[2:]
        sues[number] = {}
        for i in range(0, len(split), 2):
            # print(split[i], split[i + 1].strip(","))
            sues[number][split[i][:-1]] = int(split[i + 1].strip(","))
    for num in sues:
        sue = sues[num]
        # print(num, sue)

        children = sue.get("children", -1)
        cats = sue.get("cats", -1)
        samoyeds = sue.get("samoyeds", -1)
        pomeranians = sue.get("pomeranians", -1)
        akitas = sue.get("akitas", -1)
        vizslas = sue.get("vizslas", -1)
        goldfish = sue.get("goldfish", -1)
        trees = sue.get("trees", -1)
        cars = sue.get("cars", -1)
        perfumes = sue.get("perfumes", -1)

        if children != 3 and children != -1:
            continue
        if cats <= 7 and cats != -1:
            continue
        if samoyeds != 2 and samoyeds != -1:
            continue
        if pomeranians >= 3 and pomeranians != -1:
            continue
        if akitas != 0 and akitas != -1:
            continue
        if vizslas != 0 and vizslas != -1:
            continue
        if goldfish >= 5 and goldfish != -1:
            continue
        if trees <= 3 and trees != -1:
            continue
        if cars != 2 and cars != -1:
            continue
        if perfumes != 1 and perfumes != -1:
            continue
        return num

p2 = part2(input)
print("Part Two : " + str(p2))
