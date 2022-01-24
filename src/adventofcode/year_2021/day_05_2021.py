from fractions import Fraction
from typing import List
from typing import Tuple

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def print_board(board: List[List[int]]):
    for row in board:
        print("".join("." if x == 0 else str(x) for x in row))


def get_slope(x1: int, y1: int, x2: int, y2: int):
    x = abs(x2 - x1)
    y = abs(y2 - y1)
    if y != 0:
        slope = Fraction(x, y)
        return (slope.numerator, slope.denominator)
    return (x, y)


def fill_line(line: Tuple[Tuple[int, int], Tuple[int, int]], board: List[List[int]]):
    x1, y1 = line[0]
    x2, y2 = line[1]
    slope = get_slope(x1, y1, x2, y2)
    x_dir = 1 if x1 < x2 else -1
    y_dir = 1 if y1 < y2 else -1

    if slope[0] == 0:
        while (y_dir == 1 and y1 <= y2) or (y_dir == -1 and y1 >= y2):
            board[y1][x1] += 1
            y1 += 1 * y_dir
    elif slope[1] == 0:
        while (x_dir == 1 and x1 <= x2) or (x_dir == -1 and x1 >= x2):
            board[y1][x1] += 1
            x1 += 1 * x_dir
    else:
        while ((y_dir == 1 and y1 <= y2) or (y_dir == -1 and y1 >= y2)) or (
            (x_dir == 1 and x1 <= x2) or (x_dir == -1 and x1 >= x2)
        ):
            board[y1][x1] += 1
            x1 += slope[0] * x_dir
            y1 += slope[1] * y_dir


def map_lines(lines: List[Tuple[Tuple[int, int], Tuple[int, int]]]):
    maxX = max(max(x, x2) for (x, y), (x2, y2) in lines)
    maxY = max(max(y, y2) for (x, y), (x2, y2) in lines)

    board = [[0 for _ in range(maxX + 1)] for _ in range(maxY + 1)]

    for line in lines:
        fill_line(line, board)

    return board


@solution_timer(2021, 5, 1)
def part_one(input_data: List[str]):
    lines: List[Tuple[Tuple[int, int], Tuple[int, int]]] = []
    for line in input_data:
        p1, p2 = line.split(" -> ")
        x1, y1 = p1.split(",")
        x2, y2 = p2.split(",")
        lines.append(((int(x1), int(y1)), (int(x2), int(y2))))

    lines = [line for line in lines if line[0][0] == line[1][0] or line[0][1] == line[1][1]]

    board = map_lines(lines)
    # print_board(board)
    count = 0
    for row in board:
        for num in row:
            if num > 1:
                count += 1
    return count


@solution_timer(2021, 5, 2)
def part_two(input_data: List[str]):
    lines: List[Tuple[Tuple[int, int], Tuple[int, int]]] = []
    for line in input_data:
        p1, p2 = line.split(" -> ")
        x1, y1 = p1.split(",")
        x2, y2 = p2.split(",")
        lines.append(((int(x1), int(y1)), (int(x2), int(y2))))

    board = map_lines(lines)
    # print_board(board)
    count = 0
    for row in board:
        for num in row:
            if num > 1:
                count += 1
    return count


if __name__ == "__main__":
    data = get_input_for_day(2021, 5)
    part_one(data)
    part_two(data)
