from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def is_valid(preamble: List[int], number: int):
    for num in preamble:
        if num > number:
            continue
        needed = number - num
        count = preamble.count(needed)
        if (num == needed and count > 1) or (num != needed and count > 0):
            return True
    return False


@solution_timer(2020, 9, 1)
def part_one(input_data: List[str], preamble_length: int = 25):
    nums = [int(x) for x in input_data]
    cur_pos = preamble_length

    while cur_pos < len(nums):
        if is_valid(nums[cur_pos - preamble_length : cur_pos], nums[cur_pos]):
            cur_pos += 1
        else:
            return nums[cur_pos]

    raise SolutionNotFoundException(2020, 9, 1)


def find_continuous_sum(nums: List[int], target: int):
    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            if cur_sum == target:
                return nums[i : j + 1]
            if cur_sum > target:
                break

    return []


@solution_timer(2020, 9, 2)
def part_two(input_data: List[str], preamble_length: int = 25):
    nums = [int(x) for x in input_data]
    cur_pos = preamble_length

    while cur_pos < len(nums):
        if is_valid(nums[cur_pos - preamble_length : cur_pos], nums[cur_pos]):
            cur_pos += 1
        else:
            break

    cont_sum = find_continuous_sum(nums, nums[cur_pos])

    if len(cont_sum) == 0:
        raise SolutionNotFoundException(2020, 9, 2)

    return min(cont_sum) + max(cont_sum)


if __name__ == "__main__":
    data = get_input_for_day(2020, 9)
    part_one(data)
    part_two(data)
