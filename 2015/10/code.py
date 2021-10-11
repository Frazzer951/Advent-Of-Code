# Advent of code Year 2015 Day 10 solution
# Author = Frazzer951
# Date = October 2021

from itertools import groupby

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


# My Answer
# def lookAndSay(number):
#     newNumber = ""
#     while number:
#         count = 0
#         char = number[0]
#         for i in range(len(number)):
#             if number[i] == char:
#                 count += 1
#             else:
#                 break
#         newNumber += str(count) + char
#         number = number[count:]
#     return newNumber

# Fast Answer
def lookAndSay(number):
    return "".join([str(len(list(g))) + k for k, g in groupby(number)])


def part1(input, times):
    for _ in range(times):
        input = lookAndSay(input)
    return input


t1 = part1("1", 5)
print("Part One Test 1: " + str(t1))

p1 = part1(input[0], 40)
print("Part One : " + str(len(p1)))

p2 = part1(p1, 10)
print("Part Two : " + str(len(p2)))