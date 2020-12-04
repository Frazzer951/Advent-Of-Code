# Advent of code Year 2020 Day 2 solution
# Author = Frazzer951
# Date = December 2020

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.readlines()

num_valid = 0
for line in input:
    parts = line.split()

    min_max = parts[0].split("-")
    min_n = int(min_max[0])
    max_n = int(min_max[1])
    char = parts[1][0]
    string = parts[2]

    count = string.count(char)
    if count >= min_n and count <= max_n:
        num_valid += 1
print("Part One : " + str(num_valid))


num_valid = 0
for line in input:
    parts = line.split()

    indexes = parts[0].split("-")
    index1 = int(indexes[0])
    index2 = int(indexes[1])
    char = parts[1][0]
    string = parts[2]

    if string[index1 - 1] == char and string[index2 - 1] != char:
        num_valid += 1
    elif string[index1 - 1] != char and string[index2 - 1] == char:
        num_valid += 1
print("Part Two : " + str(num_valid))
