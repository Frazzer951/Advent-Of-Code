# Advent of code Year 2016 Day 2 solution
# Author = Frazzer951
# Date = November 2021

import math

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")

print(input)


def decipherCode(input, keypad=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], x=1, y=1):
    code = ""
    for line in input:
        for dir in line:
            if dir == "U":
                if y > 0 and keypad[y - 1][x] != None:
                    y -= 1
            elif dir == "D":
                if y < len(keypad) - 1 and keypad[y + 1][x] != None:
                    y += 1
            elif dir == "L":
                if x > 0 and keypad[y][x - 1] != None:
                    x -= 1
            elif dir == "R":
                if x < len(keypad[0]) - 1 and keypad[y][x + 1] != None:
                    x += 1
        code += str(keypad[y][x])
    return code


t1 = decipherCode(["ULL", "RRDDD", "LURDL", "UUUUD"])
print("Part One Test 1: " + str(t1))
assert t1 == "1985"

p1 = decipherCode(input)
print("Part One : " + str(p1))

keypad = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, "A", "B", "C", None],
    [None, None, "D", None, None],
]
t3 = decipherCode(["ULL", "RRDDD", "LURDL", "UUUUD"], keypad, 0, 2)
print("Part Two Test 1: " + str(t3))
assert t3 == "5DB3"

p2 = decipherCode(input, keypad, 0, 2)
print("Part Two : " + str(p2))
