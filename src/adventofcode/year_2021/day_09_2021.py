from typing import List, Dict, Tuple

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

from collections import defaultdict


@solution_timer(2021, 9, 1)
def part_one(input_data: List[str]):
    input_data = [[int(x) for x in row] for row in input_data]

    risk_level = 0

    for j in range(len(input_data)):
        for i in range(len(input_data[j])):
            if j - 1 >= 0:
                if input_data[j - 1][i] <= input_data[j][i]:
                    continue
            if j + 1 < len(input_data):
                if input_data[j + 1][i] <= input_data[j][i]:
                    continue
            if i - 1 >= 0:
                if input_data[j][i - 1] <= input_data[j][i]:
                    continue
            if i + 1 < len(input_data[j]):
                if input_data[j][i + 1] <= input_data[j][i]:
                    continue
            risk_level += input_data[j][i] + 1
            # print(f"{input_data[j][i]}: {j} {i}")
    return risk_level


def get_next_pos(x: int, y: int, input_data: List[List[int]]):
    if y - 1 >= 0:
        if input_data[y - 1][x] <= input_data[y][x]:
            return (x, y - 1)
    if y + 1 < len(input_data):
        if input_data[y + 1][x] <= input_data[y][x]:
            return (x, y + 1)
    if x - 1 >= 0:
        if input_data[y][x - 1] <= input_data[y][x]:
            return (x - 1, y)
    if x + 1 < len(input_data[y]):
        if input_data[y][x + 1] <= input_data[y][x]:
            return (x + 1, y)
    return (x, y)


def num_point_lead_here(x: int, y: int, flow: Dict[Tuple[int, int], List[Tuple[int, int]]]):
    count = 0
    points = flow.get((x, y), [])
    count += len(points)
    for point in points:
        count += num_point_lead_here(point[0], point[1], flow)
    return count


@solution_timer(2021, 9, 2)
def part_two(input_data: List[str]):
    input_data = [[int(x) for x in row] for row in input_data]

    flow = defaultdict(list)
    low_points = []

    for j in range(len(input_data)):
        for i in range(len(input_data[j])):
            if input_data[j][i] == 9:
                continue
            next_pos = get_next_pos(i, j, input_data)
            if input_data[next_pos[1]][next_pos[0]] == 9:
                raise SolutionNotFoundException(2021, 9, 2)
            if next_pos == (i, j):
                low_points.append((i, j))
            else:
                flow[next_pos].append((i, j))

    basin_sizes = []

    for point in low_points:
        # Count all the points that flow to this point
        basin_sizes.append(num_point_lead_here(point[0], point[1], flow) + 1)

    basin_sizes.sort(reverse=True)
    if len(basin_sizes) < 3:
        raise SolutionNotFoundException(2021, 9, 2)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


if __name__ == "__main__":
    data = get_input_for_day(2021, 9)
    part_one(data)
    part_two(data)
