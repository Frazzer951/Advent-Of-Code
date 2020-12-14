# Advent of code Year 2020 Day 12 solution
# Author = Frazzer951
# Date = December 2020

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def int_dir(directions):
    direction = 1
    north = 0
    south = 0
    east = 0
    west = 0
    for line in directions:
        comand = line[:1]
        number = int(line[1:])
        if comand == "N":
            north += number
        if comand == "S":
            south += number
        if comand == "E":
            east += number
        if comand == "W":
            west += number
        if comand == "L":
            turn_num = number / 90
            direction = (direction - turn_num) % 4
        if comand == "R":
            turn_num = number / 90
            direction = (direction + turn_num) % 4
        if comand == "F":
            if direction == 0:
                north += number
            if direction == 1:
                east += number
            if direction == 2:
                south += number
            if direction == 3:
                west += number
    return abs(north - south) + abs(east - west)


test_input = """F10
N3
F7
R90
F11""".split(
    "\n"
)
print("Test input : " + str(int_dir(test_input)))


print("Part One : " + str(int_dir(input)))


print("Part Two : " + str(None))
