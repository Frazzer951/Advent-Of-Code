# Advent of code Year 2015 Day 17 solution
# Author = Frazzer951
# Date = October 2021

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def part1(containers, amount):
    if len(containers) == 0:
        return 0

    first = containers[0]
    remaining = containers[1:]

    if first > amount:
        with_first = 0
    elif first == amount:
        with_first = 1
    else:
        with_first = part1(remaining, amount - first)

    return with_first + part1(remaining, amount)


t1 = part1([20, 15, 10, 5, 5], 25)
print("Part One Test 1: " + str(t1))
assert t1 == 4

input = [int(x) for x in input]

p1 = part1(input, 150)
print("Part One : " + str(p1))


def part2(containers, amount, used=0):
    if len(containers) == 0:
        return 0

    first = containers[0]
    remaining = containers[1:]

    if first > amount:
        with_first = 0
    elif first == amount:
        sizes.append(used + 1)
        with_first = 1
    else:
        with_first = part2(remaining, amount - first, used + 1)

    return with_first + part2(remaining, amount, used)


sizes = []
part2([20, 15, 10, 5, 5], 25)
t3 = sum(min(sizes) == size for size in sizes)
print("Part Two Test 1: " + str(t3))
assert t3 == 3

sizes = []
part2(input, 150)
p2 = sum(min(sizes) == size for size in sizes)
print("Part Two : " + str(p2))