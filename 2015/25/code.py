# Advent of code Year 2015 Day 25 solution
# Author = Frazzer951
# Date = October 2021

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")

input = input[0].split()


def getCode(x, y):
    pos = (x + y - 2) * (x + y - 1) // 2 + y - 1

    val = 20151125

    for i in range(pos):
        val = val * 252533 % 33554393

    return val


t1 = getCode(1, 1)
print("Part One Test 1: " + str(t1))
assert t1 == 20151125
t2 = getCode(2, 1)
print("Part One Test 2: " + str(t2))
assert t2 == 31916031
t3 = getCode(5, 3)
print("Part One Test 2: " + str(t2))
assert t3 == 28094349

x = int(input[-3].strip(","))
y = int(input[-1].strip("."))
p1 = getCode(x, y)
print("Part One : " + str(p1))
