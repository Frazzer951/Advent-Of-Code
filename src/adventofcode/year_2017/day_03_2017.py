from itertools import count
from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2017, 3, 1)
def part_one(input_data: List[str]):
    data = int(input_data[0])
    x = y = dx = 0
    dy = -1
    step = 0
    while True:
        step += 1
        if data == step:
            return abs(x) + abs(y)
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy


def sum_spiral():
    a, i, j = {(0, 0): 1}, 0, 0
    for s in count(1, 2):
        for (ds, di, dj) in [(0, 1, 0), (0, 0, -1), (1, -1, 0), (1, 0, 1)]:
            for _ in range(s + ds):
                i += di
                j += dj
                a[i, j] = sum(a.get((n, m), 0) for n in range(i - 1, i + 2) for m in range(j - 1, j + 2))
                yield a[i, j]


@solution_timer(2017, 3, 2)
def part_two(input_data: List[str]):
    data = int(input_data[0])
    for x in sum_spiral():
        if x > data:
            return x


if __name__ == "__main__":
    data = get_input_for_day(2017, 3)
    part_one(data)
    part_two(data)
