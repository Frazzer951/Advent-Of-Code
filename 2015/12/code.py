# Advent of code Year 2015 Day 12 solution
# Author = Frazzer951
# Date = October 2021

import json

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = json.load(input_file)


def sum_of_nums(item, skipRed=False):
    if isinstance(item, list):
        return sum([sum_of_nums(i, skipRed) for i in item])
    if isinstance(item, dict):
        if skipRed and "red" in item.values():
            return 0
        return sum([sum_of_nums(i, skipRed) for i in item.values()])
    if isinstance(item, int):
        return item
    return 0


assert sum_of_nums([1, 2, 3]) == 6
assert sum_of_nums({"a": 2, "b": 4}) == 6
assert sum_of_nums([[[3]]]) == 3
assert sum_of_nums({"a": {"b": 4}, "c": -1}) == 3
assert sum_of_nums({"a": [-1, 1]}) == 0
assert sum_of_nums([-1, {"a": 1}]) == 0
assert sum_of_nums([]) == 0
assert sum_of_nums({}) == 0

p1 = sum_of_nums(input)
print("Part One : " + str(p1))

assert sum_of_nums([1, 2, 3], True) == 6
assert sum_of_nums([1, {"c": "red", "b": 2}, 3], True) == 4
assert sum_of_nums({"d": "red", "e": [1, 2, 3, 4], "f": 5}, True) == 0
assert sum_of_nums([1, "red", 5], True) == 6

p2 = sum_of_nums(input, True)
print("Part Two : " + str(p2))