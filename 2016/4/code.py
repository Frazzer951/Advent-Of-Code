# Advent of code Year 2016 Day 4 solution
# Author = Frazzer951
# Date = November 2021

from collections import Counter

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def is_real(code):
    name = code.rsplit("-", 1)[0].replace("-", "")
    id = code.rsplit("-", 1)[1].split("[", 1)[0]
    checksum = code.split("[")[-1].strip("]")
    checksum = list(checksum)

    letters = Counter(name)
    most_common = sorted(letters.most_common(), key=lambda x: (-x[1], x[0]))
    most_common = [x[0] for x in most_common]
    most_common = most_common[:5]

    if most_common != checksum:
        return False
    return True


def part1(input):
    id_sum = 0
    for code in input:
        if is_real(code):
            id_sum += int(code.split("-")[-1].split("[")[0])
    return id_sum


assert is_real("aaaaa-bbb-z-y-x-123[abxyz]") == True
assert is_real("a-b-c-d-e-f-g-h-987[abcde]") == True
assert is_real("not-a-real-room-404[oarel]") == True
assert is_real("totally-real-room-200[decoy]") == False

t1 = part1(
    [
        "aaaaa-bbb-z-y-x-123[abxyz]",
        "a-b-c-d-e-f-g-h-987[abcde]",
        "not-a-real-room-404[oarel]",
        "totally-real-room-200[decoy]",
    ]
)
print("Part One Test 1: " + str(t1))
assert t1 == 1514

p1 = part1(input)
print("Part One : " + str(p1))


def decrpyt_name(code):
    name = code.rsplit("-", 1)[0]
    id = int(code.split("-")[-1].split("[")[0])
    new_name = ""
    for letter in name:
        if letter == "-":
            new_name += " "
        else:
            char = ord(letter) - 97
            new_char = (char + id) % 26
            new_char += 97
            new_name += chr(new_char)
    return new_name


def part2(input):
    for code in input:
        if is_real(code):
            name = decrpyt_name(code)
            if name == "northpole object storage":
                return int(code.split("-")[-1].split("[")[0])
    return -1


name = decrpyt_name("qzmt-zixmtkozy-ivhz-343[zimth]")
assert name == "very encrypted name"

p2 = part2(input)
print("Part Two : " + str(p2))
