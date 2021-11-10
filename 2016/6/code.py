# Advent of code Year 2016 Day 6 solution
# Author = Frazzer951
# Date = November 2021

from collections import Counter

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def decodeMessage(input, part2=False):
    counters = [Counter() for _ in range(len(input[0]))]
    for row in input:
        for i, char in enumerate(row):
            counters[i][char] += 1
    if not part2:
        message = [x.most_common(1)[0][0] for x in counters]
    else:
        message = [x.most_common()[-1][0] for x in counters]
    return "".join(message)


t1 = decodeMessage(
    [
        "eedadn",
        "drvtee",
        "eandsr",
        "raavrd",
        "atevrs",
        "tsrnev",
        "sdttsa",
        "rasrtv",
        "nssdts",
        "ntnada",
        "svetve",
        "tesnvt",
        "vntsnd",
        "vrdear",
        "dvrsen",
        "enarar",
    ]
)
print("Part One Test 1: " + str(t1))
assert t1 == "easter"

p1 = decodeMessage(input)
print("Part One : " + str(p1))


t3 = decodeMessage(
    [
        "eedadn",
        "drvtee",
        "eandsr",
        "raavrd",
        "atevrs",
        "tsrnev",
        "sdttsa",
        "rasrtv",
        "nssdts",
        "ntnada",
        "svetve",
        "tesnvt",
        "vntsnd",
        "vrdear",
        "dvrsen",
        "enarar",
    ],
    True,
)
print("Part Two Test 1: " + str(t3))
assert t3 == "advent"

p2 = decodeMessage(input, True)
print("Part Two : " + str(p2))
