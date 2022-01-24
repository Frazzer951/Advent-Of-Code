from collections import deque
from typing import Deque
from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def is_valid_chunk(chunk: str):
    openChar = ["(", "[", "{", "<"]
    closeChar = [")", "]", "}", ">"]
    nextCloseChar: Deque[str] = deque()
    for i in range(len(chunk)):
        if chunk[i] in openChar:
            nextCloseChar.append(closeChar[openChar.index(chunk[i])])
        elif chunk[i] in closeChar:
            if chunk[i] != nextCloseChar[-1]:
                return i
            nextCloseChar.pop()
    missing = "".join(nextCloseChar)[::-1]
    return missing


@solution_timer(2021, 10, 1)
def part_one(input_data: List[str]):
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0
    for line in input_data:
        error_index = is_valid_chunk(line)
        if error_index != -1 and not isinstance(error_index, str):
            score += scores[line[error_index]]
    return score


def get_score(missing_data: str):
    scores = {")": 1, "]": 2, "}": 3, ">": 4}
    score = 0
    for char in missing_data:
        score *= 5
        score += scores[char]
    return score


@solution_timer(2021, 10, 2)
def part_two(input_data: List[str]):
    input_data = [line for line in input_data if isinstance(is_valid_chunk(line), str)]
    scores = []
    for line in input_data:
        missing_data = is_valid_chunk(line)
        score = get_score(missing_data)
        scores.append(score)
    scores.sort()
    middle = len(scores) // 2
    return scores[middle]


if __name__ == "__main__":
    data = get_input_for_day(2021, 10)
    part_one(data)
    part_two(data)
