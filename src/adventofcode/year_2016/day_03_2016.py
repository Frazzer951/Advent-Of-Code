from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2016, 3, 1)
def part_one(input_data: List[str]):
    valid_triangles = 0
    for line in input_data:
        nums = line.strip().split(" ")
        nums = [int(x) for x in nums if x != ""]
        if nums[0] + nums[1] > nums[2] and nums[1] + nums[2] > nums[0] and nums[0] + nums[2] > nums[1]:
            valid_triangles += 1
    return valid_triangles


@solution_timer(2016, 3, 2)
def part_two(input_data: List[str]):
    input = [line.strip().split(" ") for line in input_data]
    input = [[int(x) for x in line if x != ""] for line in input]

    triangles = []
    for i in range(0, len(input), 3):
        t1 = [input[i][0], input[i + 1][0], input[i + 2][0]]
        t2 = [input[i][1], input[i + 1][1], input[i + 2][1]]
        t3 = [input[i][2], input[i + 1][2], input[i + 2][2]]
        triangles.append(t1)
        triangles.append(t2)
        triangles.append(t3)

    valid_triangles = 0
    for triangle in triangles:
        if (
            triangle[0] + triangle[1] > triangle[2]
            and triangle[1] + triangle[2] > triangle[0]
            and triangle[0] + triangle[2] > triangle[1]
        ):
            valid_triangles += 1
    return valid_triangles


if __name__ == "__main__":
    data = get_input_for_day(2016, 3)
    part_one(data)
    part_two(data)
