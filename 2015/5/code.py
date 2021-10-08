# Advent of code Year 2015 Day 5 solution
# Author = Frazzer951
# Date = October 2021

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def isNice(word):
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


def part1(input):
    count = 0
    for word in input:
        if isNice(word):
            count += 1
    return count


t1 = isNice("ugknbfddgicrmopn")
print("Part One Test 1: " + str(t1))
t2 = isNice("aaa")
print("Part One Test 2: " + str(t2))
t3 = isNice("jchzalrnumimnmhp")
print("Part One Test 3: " + str(t3))
t4 = isNice("haegwjzuvuyypxyu")
print("Part One Test 4: " + str(t4))
t5 = isNice("dvszwmarrgswjxmb")
print("Part One Test 5: " + str(t5))

p1 = part1(input)
print("Part One : " + str(p1))


def isNice(word):
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
        pair = word[i : i + 2]
        if pair in word[i + 2 :]:
            return True

    return False


def part2(input):
    count = 0
    for word in input:
        if isNice(word):
            count += 1
    return count


t6 = isNice("qjhvhtzxzqqjkmpb")
print("Part Two Test 1: " + str(t6))
t7 = isNice("xxyxx")
print("Part Two Test 2: " + str(t7))
t8 = isNice("uurcxstgmygtbstg")
print("Part Two Test 3: " + str(t8))
t9 = isNice("ieodomkazucvgmuy")
print("Part Two Test 4: " + str(t9))

p2 = part2(input)
print("Part Two : " + str(p2))