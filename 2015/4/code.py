# Advent of code Year 2015 Day 4 solution
# Author = Frazzer951
# Date = October 2021

import hashlib

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def part1(input):
    for i in range(10000000):
        string = input + str(i)
        if hashlib.md5(string.encode('utf-8')).hexdigest()[:5] == "00000":
            return i
    return None


t1 = part1("abcdef")
print("Part One Test 1: " + str(t1))
t2 = part1("pqrstuv")
print("Part One Test 2: " + str(t2))

p1 = part1(input[0])
print("Part One : " + str(p1))


def part2(input):
    for i in range(10000000):
        string = input + str(i)
        if hashlib.md5(string.encode('utf-8')).hexdigest()[:6] == "000000":
            return i
    return None

p2 = part2(input[0])
print("Part Two : " + str(p2))