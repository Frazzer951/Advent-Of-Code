# Advent of code Year 2016 Day 1 solution
# Author = Frazzer951
# Date = October 2021

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")[0].split()
input = [x.strip(",") for x in input]


def rotate(dir, turn):
    if turn == "R":
        if dir == "n":
            return "e"
        elif dir == "e":
            return "s"
        elif dir == "s":
            return "w"
        elif dir == "w":
            return "n"
    elif turn == "L":
        if dir == "n":
            return "w"
        elif dir == "e":
            return "n"
        elif dir == "s":
            return "e"
        elif dir == "w":
            return "s"


def numBlocksAway(moves):
    x = 0
    y = 0
    dir = "n"
    for move in moves:
        if move[0] == "R":
            dir = rotate(dir, "R")
        elif move[0] == "L":
            dir = rotate(dir, "L")

        amount = int(move[1:])
        if dir == "n":
            y += amount
        elif dir == "e":
            x += amount
        elif dir == "s":
            y -= amount
        elif dir == "w":
            x -= amount
    return abs(x) + abs(y)


t1 = numBlocksAway(["R2", "L3"])
print("Part One Test 1: " + str(t1))
assert t1 == 5
t2 = numBlocksAway(["R2", "R2", "R2"])
print("Part One Test 2: " + str(t2))
assert t2 == 2
t3 = numBlocksAway(["R5", "L5", "R5", "R3"])
print("Part One Test 2: " + str(t3))
assert t3 == 12

p1 = numBlocksAway(input)
print("Part One : " + str(p1))


t4 = numBlocksAway(["R8", "R4", "R4", "R8"], True)
print("Part Two Test 1: " + str(t4))
assert t4 == 4, f"Expected 4 got {t4}"

p2 = numBlocksAway(input, True)
print("Part Two : " + str(p2))
