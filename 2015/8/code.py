# Advent of code Year 2015 Day 8 solution
# Author = Frazzer951
# Date = October 2021

import re

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def size_in_memory(str):
    assert str[0] == '"'
    assert str[-1] == '"'
    mem = str[1:-1]
    mem = mem.replace("\\\\", "x")
    mem = mem.replace('\\"', "x")
    mem, _ = re.subn("\\\\x..", "x", mem)
    return len(mem)


def part1(input):
    count = 0

    for line in input:
        line = line.strip()
        line_count = len(line)
        line_mem = size_in_memory(line)
        count += line_count - line_mem

    return count


t1 = part1([r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"'])
print("Part One Test 1: " + str(t1))
t2 = part1([r'"\\"', r'"\\\xe0"'])
print("Part One Test 2: " + str(t2))

p1 = part1(input)
print("Part One : " + str(p1))


def size_encoded(str):
    encoded = str
    encoded = encoded.replace("\\", "\\\\")
    encoded = encoded.replace('"', '\\"')
    encoded = '"' + encoded + '"'
    return len(encoded)


def part2(input):
    count = 0

    for line in input:
        line = line.strip()
        line_count = len(line)
        line_enc = size_encoded(line)
        count += line_enc - line_count

    return count


t3 = part2([r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"'])
print("Part Two Test 1: " + str(t3))

p2 = part2(input)
print("Part Two : " + str(p2))