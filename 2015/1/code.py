# Advent of code Year 2015 Day 1 solution
# Author = Frazzer951
# Date = October 2021

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def part1(input):
    floor = 0

    for c in input[0]:
        if c == "(":
            floor += 1
        if c == ")":
            floor -= 1
    return floor


floor = part1(input)
print("Part One : " + str(floor))


def part2(input):
    floor = 0

    for i in range(len(input[0])):
        if input[0][i] == "(":
            floor += 1
        if input[0][i] == ")":
            floor -= 1
        if floor == -1:
            return i + 1
    return -1


index = part2(input)
print("Part Two : " + str(index))

t1 = part2([")"])
t2 = part2(["()())"])
print("Part Two Test 1: " + str(t1))
print("Part Two Test 2: " + str(t2))
