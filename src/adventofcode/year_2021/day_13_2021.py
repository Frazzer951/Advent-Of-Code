from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int


@dataclass
class Fold:
    axis: str
    index: int


def print_grid(points: List[Point]):
    max_x = max(point.x for point in points)
    max_y = max(point.y for point in points)
    print("-" * max_x)
    print("\n".join("".join(u"\u25A0" if Point(x, y) in points else " " for x in range(max_x + 1)) for y in range(max_y + 1)))
    print("-" * max_x)


def fold_grid(points: List[Point], fold: Fold):
    for i, point in enumerate(points):
        if fold.axis == "x" and point.x > fold.index:
            points[i] = Point(x=2 * fold.index - point.x, y=point.y)
        elif fold.axis == "y" and point.y > fold.index:
            points[i] = Point(x=point.x, y=2 * fold.index - point.y)
    return points


@solution_timer(2021, 13, 1)
def part_one(input_data: List[str]):
    points: List[Point] = []
    folds: List[Fold] = []
    for line in input_data:
        if line == "":
            continue
        if line.startswith("fold along"):
            fold = line.split()[-1]
            axis = fold.split("=")[0]
            index = int(fold.split("=")[1])
            folds.append(Fold(axis, index))
        else:
            point = list(map(int, line.split(",")))
            points.append(Point(point[0], point[1]))

    # print_grid(points)
    points = fold_grid(points, folds[0])
    # print_grid(points)

    return len(set(points))


@solution_timer(2021, 13, 2)
def part_two(input_data: List[str]):
    points: List[Point] = []
    folds: List[Fold] = []
    for line in input_data:
        if line == "":
            continue
        if line.startswith("fold along"):
            f = line.split()[-1]
            axis = f.split("=")[0]
            index = int(f.split("=")[1])
            folds.append(Fold(axis, index))
        else:
            point = list(map(int, line.split(",")))
            points.append(Point(point[0], point[1]))

    for fold in folds:
        points = fold_grid(points, fold)

    print_grid(points)
    return len(set(points))


if __name__ == "__main__":
    data = get_input_for_day(2021, 13)
    part_one(data)
    part_two(data)
