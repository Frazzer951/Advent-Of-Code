# Advent of code Year 2015 Day 9 solution
# Author = Frazzer951
# Date = October 2021

from itertools import permutations
import math

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def part1(input):
    path = {}
    locations = []
    for line in input:
        sLine = line.split()
        c1 = sLine[0]
        c2 = sLine[2]
        dist = sLine[4]
        path[c1 + c2] = int(dist)
        path[c2 + c1] = int(dist)
        locations.append(c1)
        locations.append(c2)

    locations = set(locations)

    # print(path)
    # print(locations)
    shortest = math.inf
    for perm in permutations(locations):
        # print(perm)
        permDist = 0
        for c1, c2 in zip(perm[:-1], perm[1:]):
            permDist += path[c1 + c2]
        shortest = min(shortest, permDist)
    return shortest


t1 = part1(
    ["London to Dublin = 464", "London to Belfast = 518", "Dublin to Belfast = 141"]
)
print("Part One Test 1: " + str(t1))

p1 = part1(input)
print("Part One : " + str(p1))


def part2(input):
    path = {}
    locations = []
    for line in input:
        sLine = line.split()
        c1 = sLine[0]
        c2 = sLine[2]
        dist = sLine[4]
        path[c1 + c2] = int(dist)
        path[c2 + c1] = int(dist)
        locations.append(c1)
        locations.append(c2)

    locations = set(locations)

    # print(path)
    # print(locations)
    longest = -math.inf
    for perm in permutations(locations):
        # print(perm)
        permDist = 0
        for c1, c2 in zip(perm[:-1], perm[1:]):
            permDist += path[c1 + c2]
        longest = max(longest, permDist)
    return longest


t3 = part2(
    ["London to Dublin = 464", "London to Belfast = 518", "Dublin to Belfast = 141"]
)
print("Part Two Test 1: " + str(t3))

p2 = part2(input)
print("Part Two : " + str(p2))