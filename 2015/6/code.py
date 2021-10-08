# Advent of code Year 2015 Day 6 solution
# Author = Frazzer951
# Date = October 2021

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def part1(input):
    lights = [[False for _ in range(1000)] for _ in range(1000)]
    for line in input:
        line = line.split()
        if line[0] == "turn":
            if line[1] == "on":
                x1, y1 = line[2].split(",")
                x2, y2 = line[4].split(",")
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                for i in range(x1, x2 + 1):
                    for j in range(y1, y2 + 1):
                        lights[i][j] = True
            if line[1] == "off":
                x1, y1 = line[2].split(",")
                x2, y2 = line[4].split(",")
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                for i in range(x1, x2 + 1):
                    for j in range(y1, y2 + 1):
                        lights[i][j] = False
        if line[0] == "toggle":
            x1, y1 = line[1].split(",")
            x2, y2 = line[3].split(",")
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    lights[i][j] = not lights[i][j]
    return sum(x.count(True) for x in lights)


t1 = part1(["turn on 0,0 through 999,999"])
print("Part One Test 1: " + str(t1))
t2 = part1(["toggle 0,0 through 999,0"])
print("Part One Test 2: " + str(t2))
t3 = part1(["turn off 499,499 through 500,500"])
print("Part One Test 3: " + str(t3))

p1 = part1(input)
print("Part One : " + str(p1))


def part2(input):
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in input:
        line = line.split()
        if line[0] == "turn":
            if line[1] == "on":
                x1, y1 = line[2].split(",")
                x2, y2 = line[4].split(",")
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                for i in range(x1, x2 + 1):
                    for j in range(y1, y2 + 1):
                        lights[i][j] += 1
            if line[1] == "off":
                x1, y1 = line[2].split(",")
                x2, y2 = line[4].split(",")
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                for i in range(x1, x2 + 1):
                    for j in range(y1, y2 + 1):
                        lights[i][j] -= 1
                        if lights[i][j] < 0:
                            lights[i][j] = 0
        if line[0] == "toggle":
            x1, y1 = line[1].split(",")
            x2, y2 = line[3].split(",")
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    lights[i][j] += 2
    return sum(sum(lights, []))


t4 = part2(["turn on 0,0 through 0,0"])
print("Part Two Test 1: " + str(t4))
t5 = part2(["toggle 0,0 through 999,999"])
print("Part Two Test 2: " + str(t5))

p2 = part2(input)
print("Part Two : " + str(p2))