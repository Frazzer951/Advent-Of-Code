# Advent of code Year 2015 Day 20 solution
# Author = Frazzer951
# Date = October 2021

import math

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def firstHouseOverNum(n):
    house = [0] * int(n / 10)
    for i in range(1, int(n / 10)):
        for j in range(i, int(n / 10), i):
            house[j] += i * 10
    for i in range(len(house)):
        if house[i] >= n:
            return i


p1 = firstHouseOverNum(33100000)
print("Part One : " + str(p1))


def firstHouseOverNum2(n):
    house = [0] * int(n / 10)
    for i in range(1, int(n / 10)):
        for j in range(i, min(int(n / 10), 50 * i), i):
            house[j] += i * 11
    for i in range(len(house)):
        if house[i] >= n:
            return i


p2 = firstHouseOverNum2(33100000)
print("Part Two : " + str(p2))