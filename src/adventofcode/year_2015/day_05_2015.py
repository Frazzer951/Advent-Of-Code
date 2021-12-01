from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def isNice_1(word):
    vowels = ["a", "e", "i", "o", "u"]
    not_allowed = ["ab", "cd", "pq", "xy"]
    for c in not_allowed:
        if c in word:
            return False

    vowel_count = 0
    doubleLetter = False
    n = len(word)
    for i in range(n):
        if word[i] in vowels:
            vowel_count += 1
        if i + 1 < n and word[i] == word[i + 1]:
            doubleLetter = True

        if vowel_count >= 3 and doubleLetter:
            return True
    return False


@solution_timer(2015, 5, 1)
def part_one(input_data: List[str]):
    count = 0
    for word in input_data:
        if isNice_1(word):
            count += 1
    return count


def isNice_2(word):
    repeated = False
    n = len(word)
    for i in range(n):
        if i + 2 < n and word[i] == word[i + 2]:
            repeated = True
        if repeated:
            break
    if not repeated:
        return False
    for i in range(n):
        pair = word[i: i + 2]
        if pair in word[i + 2:]:
            return True

    return False


@solution_timer(2015, 5, 2)
def part_two(input_data: List[str]):
    count = 0
    for word in input_data:
        if isNice_2(word):
            count += 1
    return count


if __name__ == "__main__":
    data = get_input_for_day(2015, 5)
    part_one(data)
    part_two(data)
