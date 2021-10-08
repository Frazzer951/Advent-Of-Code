# Advent of code Year 2015 Day 3 solution
# Author = Frazzer951
# Date = October 2021

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def part1(input):
    x, y = 0, 0
    visited = set()
    visited.add((x, y))

    for dir in input[0]:
        if dir == "^":
            y += 1
        if dir == ">":
            x += 1
        if dir == "v":
            y -= 1
        if dir == "<":
            x -= 1
        visited.add((x, y))
    return len(visited)


t1 = part1([">"])
print("Part One Test 1: " + str(t1))
t2 = part1(["^>v<"])
print("Part One Test 2: " + str(t2))
t3 = part1(["^v^v^v^v^v"])
print("Part One Test 2: " + str(t3))

p1 = part1(input)
print("Part One : " + str(p1))


def part2(input):
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    visited = set()
    visited.add((x1, y1))
    visited.add((x2, y2))

    santa = True

    for dir in input[0]:
        if dir == "^":
            if santa:
                y1 += 1
            else:
                y2 += 1
        if dir == ">":
            if santa:
                x1 += 1
            else:
                x2 += 1
        if dir == "v":
            if santa:
                y1 -= 1
            else:
                y2 -= 1
        if dir == "<":
            if santa:
                x1 -= 1
            else:
                x2 -= 1
        if santa:
            visited.add((x1, y1))
        else:
            visited.add((x2, y2))
        santa = not santa
    return len(visited)


t4 = part2(["^v"])
print("Part Two Test 1: " + str(t4))
t5 = part2(["^>v<"])
print("Part Two Test 2: " + str(t5))
t6 = part2(["^v^v^v^v^v"])
print("Part Two Test 2: " + str(t6))

p2 = part2(input)
print("Part Two : " + str(p2))