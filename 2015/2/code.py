# Advent of code Year 2015 Day 2 solution
# Author = Frazzer951
# Date = October 2021

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def part1(input):
    area = 0

    for line in input:
        sides = line.split("x")
        sides = [int(x) for x in sides]
        s1 = sides[0] * sides[1]
        s2 = sides[1] * sides[2]
        s3 = sides[2] * sides[0]
        smallest = min(s1, s2, s3)
        area += (2 * s1 + 2 * s2 + 2 * s3) + smallest

    return area


t1 = part1(["2x3x4"])
t2 = part1(["1x1x10"])
print("Part One Test 1: " + str(t1))
print("Part One Test 2: " + str(t2))

area = part1(input)
print("Part One : " + str(area))


def part2(input):
    length = 0

    for line in input:
        sides = line.split("x")
        sides = [int(x) for x in sides]
        sides = sorted(sides)
        length += 2 * sides[0] + 2 * sides[1] + (sides[0] * sides[1] * sides[2])

    return length


t3 = part2(["2x3x4"])
t4 = part2(["1x1x10"])
print("Part Two Test 1: " + str(t3))
print("Part Two Test 2: " + str(t4))

length = part2(input)
print("Part Two : " + str(length))
