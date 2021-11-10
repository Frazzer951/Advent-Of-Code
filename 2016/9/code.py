# Advent of code Year 2016 Day 9 solution
# Author = Frazzer951
# Date = November 2021

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")
input = input[0]


def part1(input):
    decompressed = ""
    i = 0
    while i < len(input):
        if input[i] == "(":
            marker_close = input.find(")", i)
            marker = input[i + 1 : marker_close]
            marker = marker.split("x")
            length = int(marker[0])
            repeat = int(marker[1])
            decompressed += input[marker_close + 1 : marker_close + 1 + length] * repeat
            i = marker_close + length + 1
        else:
            decompressed += input[i]
            i += 1
    return decompressed


part1_tests = [
    ("ADVENT", "ADVENT"),
    ("A(1x5)BC", "ABBBBBC"),
    ("(3x3)XYZ", "XYZXYZXYZ"),
    ("A(2x2)BCD(2x2)EFG", "ABCBCDEFEFG"),
    ("(6x1)(1x3)A", "(1x3)A"),
    ("X(8x2)(3x3)ABCY", "X(3x3)ABC(3x3)ABCY"),
]
for test in part1_tests:
    result = part1(test[0])
    assert result == test[1], f"{result} is not {test[1]}"


p1 = part1(input)
print("Part One : " + str(len(p1)))


def part2(input):
    if "(" not in input:
        return len(input)
    ret = 0
    while "(" in input:
        ret += input.find("(")
        input = input[input.find("(") :]
        marker = input[1 : input.find(")")].split("x")
        input = input[input.find(")") + 1 :]
        ret += part2(input[: int(marker[0])]) * int(marker[1])
        input = input[int(marker[0]) :]
    ret += len(input)
    return ret


part2_tests = [
    ("(3x3)XYZ", 9),
    ("X(8x2)(3x3)ABCY", 20),
    ("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920),
    ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445),
]
for test in part2_tests:
    result = part2(test[0])
    assert result == test[1], f"{result} is not {test[1]}"

p2 = part2(input)
print("Part Two : " + str(p2))
