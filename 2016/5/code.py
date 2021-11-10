# Advent of code Year 2016 Day 5 solution
# Author = Frazzer951
# Date = November 2021

import hashlib

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")
input = input[0]


def part1(input):
    counter = 0
    code = ""
    while len(code) < 8:
        result = hashlib.md5(input.encode() + str(counter).encode())
        if result.hexdigest()[:5] == "00000":
            code += result.hexdigest()[5]
            print(code)
        counter += 1
    return code


# t1 = part1("abc")
# print("Part One Test 1: " + str(t1))
# assert t1 == "18f47a30"
#
# p1 = part1(input)
# print("Part One : " + str(p1))


def part2(input):
    counter = 0
    code = ["_"] * 8
    while "_" in code:
        result = hashlib.md5(input.encode() + str(counter).encode())
        if result.hexdigest()[:5] == "00000":
            pos = result.hexdigest()[5]
            if pos in "01234567" and code[int(pos)] == "_":
                code[int(pos)] = result.hexdigest()[6]
                print("".join(code))
        counter += 1
    return "".join(code)


t3 = part2("abc")
print("Part Two Test 1: " + str(t3))
assert t3 == "05ace8e3"

p2 = part2(input)
print("Part Two : " + str(p2))
