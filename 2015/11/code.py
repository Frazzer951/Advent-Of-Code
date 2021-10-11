# Advent of code Year 2015 Day 11 solution
# Author = Frazzer951
# Date = October 2021

import re

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")

alp = "abcdefghijklmnopqrstuvwxyz"
consecutive = [alp[i : i + 3] for i in range(24)]
inc = {"z": "a"}
for i in range(25):
    inc[alp[i]] = alp[i + 1]


def checkPass1(password):
    password = password.strip()
    passRule1 = False
    for set in consecutive:
        if set in password:
            passRule1 = True
            break
    rule2 = re.search("i|o|l", password)
    rule3 = re.fullmatch(".*(.)\\1.*(.)\\2.*", password)
    return passRule1 and rule2 is None and rule3


def incrementPass(password):
    password = password[:-1] + inc[password[-1]]
    for i in range(-1, -8, -1):
        if password[i] == "a":
            password = password[: i - 1] + inc[password[i - 1]] + password[i:]
        else:
            break
    return password


def part1(input):
    newPass = input

    while True:
        newPass = incrementPass(newPass)
        if checkPass1(newPass):
            break

    return newPass


t1 = checkPass1("hijklmmn")
print("Part One Test 1: " + str(t1))
t2 = checkPass1("abbceffg")
print("Part One Test 2: " + str(t2))
t3 = checkPass1("abbcegjk")
print("Part One Test 2: " + str(t3))
t4 = part1("abcdefgh")
print("Part One Test 2: " + str(t4))
t5 = part1("ghijklmn")
print("Part One Test 2: " + str(t5))
assert t1 == False
assert t2 == False
assert t3 == False
assert t4 == "abcdffaa"
assert t5 == "ghjaabcc"

p1 = part1(input[0])
print("Part One : " + str(p1))


p2 = part1(p1)
print("Part Two : " + str(p2))