from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2015, 6, 1)
def part_one(input_data: List[str]):
    lights = [[False for _ in range(1000)] for _ in range(1000)]
    for line in input_data:
        command = line.split()
        if command[0] == "turn":
            if command[1] == "on":
                p1 = command[2].split(",")
                p2 = command[4].split(",")
                x1, y1, x2, y2 = int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1])
                for i in range(x1, x2 + 1):
                    for j in range(y1, y2 + 1):
                        lights[i][j] = True
            if command[1] == "off":
                p1 = command[2].split(",")
                p2 = command[4].split(",")
                x1, y1, x2, y2 = int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1])
                for i in range(x1, x2 + 1):
                    for j in range(y1, y2 + 1):
                        lights[i][j] = False
        if command[0] == "toggle":
            p1 = command[1].split(",")
            p2 = command[3].split(",")
            x1, y1, x2, y2 = int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1])
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    lights[i][j] = not lights[i][j]
    return sum(x.count(True) for x in lights)


@solution_timer(2015, 6, 2)
def part_two(input_data: List[str]):
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in input_data:
        command = line.split()
        if command[0] == "turn":
            if command[1] == "on":
                p1 = command[2].split(",")
                p2 = command[4].split(",")
                x1, y1, x2, y2 = int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1])
                for i in range(x1, x2 + 1):
                    for j in range(y1, y2 + 1):
                        lights[i][j] += 1
            if command[1] == "off":
                p1 = command[2].split(",")
                p2 = command[4].split(",")
                x1, y1, x2, y2 = int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1])
                for i in range(x1, x2 + 1):
                    for j in range(y1, y2 + 1):
                        lights[i][j] -= 1
                        if lights[i][j] < 0:
                            lights[i][j] = 0
        if command[0] == "toggle":
            p1 = command[1].split(",")
            p2 = command[3].split(",")
            x1, y1, x2, y2 = int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1])
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    lights[i][j] += 2
    return sum(sum(lights, []))


if __name__ == "__main__":
    data = get_input_for_day(2015, 6)
    part_one(data)
    part_two(data)
