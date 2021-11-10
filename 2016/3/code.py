# Advent of code Year 2016 Day 3 solution
# Author = Frazzer951
# Date = November 2021

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def part1(input):
    valid_triangles = 0
    for line in input:
        nums = line.strip().split(" ")
        nums = [int(x) for x in nums if x != ""]
        if (
            nums[0] + nums[1] > nums[2]
            and nums[1] + nums[2] > nums[0]
            and nums[0] + nums[2] > nums[1]
        ):
            valid_triangles += 1
    return valid_triangles


t1 = part1(["5 10 25"])
print("Part One Test 1: " + str(t1))
assert t1 == 0

p1 = part1(input)
print("Part One : " + str(p1))


def part2(input):
    input = [line.strip().split(" ") for line in input]
    input = [[int(x) for x in line if x != ""] for line in input]

    triangles = []
    for i in range(0, len(input), 3):
        t1 = [input[i][0], input[i + 1][0], input[i + 2][0]]
        t2 = [input[i][1], input[i + 1][1], input[i + 2][1]]
        t3 = [input[i][2], input[i + 1][2], input[i + 2][2]]
        triangles.append(t1)
        triangles.append(t2)
        triangles.append(t3)

    valid_triangles = 0
    for triangle in triangles:
        if (
            triangle[0] + triangle[1] > triangle[2]
            and triangle[1] + triangle[2] > triangle[0]
            and triangle[0] + triangle[2] > triangle[1]
        ):
            valid_triangles += 1
    return valid_triangles


p2 = part2(input)
print("Part Two : " + str(p2))
