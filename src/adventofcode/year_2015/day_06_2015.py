from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2015, 6, 1)
def part_one(input_data: List[str]):
    lights = [[False for _ in range(1000)] for _ in range(1000)]
    for line in input_data:
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


@solution_timer(2015, 6, 2)
def part_two(input_data: List[str]):
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in input_data:
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


if __name__ == "__main__":
    data = get_input_for_day(2015, 6)
    part_one(data)
    part_two(data)
