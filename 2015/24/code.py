# Advent of code Year 2015 Day 24 solution
# Author = Frazzer951
# Date = October 2021

from functools import reduce
from itertools import combinations
from operator import mul

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")
nums = [int(i) for i in input]


def splitPresents(weights, num_groups):
    group_size = sum(weights) // num_groups
    for i in range(len(weights)):
        qes = [reduce(mul, c) for c in combinations(weights, i) if sum(c) == group_size]
        if qes:
            return min(qes)


t1 = splitPresents([1, 2, 3, 4, 5, 7, 8, 9, 10, 11], 3)
print("Part One Test 1: " + str(t1))
assert t1 == 99

p1 = splitPresents(nums, 3)
print("Part One : " + str(p1))

t3 = splitPresents([1, 2, 3, 4, 5, 7, 8, 9, 10, 11], 4)
print("Part Two Test 1: " + str(t3))
assert t3 == 44

p2 = splitPresents(nums, 4)
print("Part Two : " + str(p2))
