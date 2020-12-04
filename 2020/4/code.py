# Advent of code Year 2020 Day 4 solution
# Author = Frazzer951
# Date = December 2020
import re

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.readlines()

passports = []

requirements = [
    "byr",  # (Birth Year)
    "iyr",  # (Issue Year)
    "eyr",  # (Expiration Year)
    "hgt",  # (Height)
    "hcl",  # (Hair Color)
    "ecl",  # (Eye Color)
    "pid",  # (Passport ID)
    # "cid",  # (Country ID)
]

hex_char = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
]

eye_col = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

string = ""
for line in input:
    if line == "\n":
        passports.append(string)
        string = ""
    else:
        string = string + " " + line.strip("\n")
passports.append(string)

count = 0
for passport in passports:
    valid = True
    for req in requirements:
        if req not in passport:
            valid = False
            #print("Not Valid, {} not in string {}".format(req, passport))
            continue
    if valid:
        count += 1

print("Part One : " + str(count))


count = 0
for passport in passports:
    valid = True
    for req in requirements:
        if req not in passport:
            valid = False
            continue

    if not valid:
        continue

    if "byr" in passport:
        index = passport.index("byr")
        year = int(passport[index + 4 : index + 8])
        # print(year)
        if not (year >= 1920 and year <= 2002):
            # print("byr {} is not between 1920 and 2002".format(year))
            continue

    if "iyr" in passport:
        index = passport.index("iyr")
        year = int(passport[index + 4 : index + 8])
        # print(year)
        if not (year >= 2010 and year <= 2020):
            # print("iyr {} is not between 2010 and 2020".format(year))
            continue

    if "eyr" in passport:
        index = passport.index("eyr")
        year = int(passport[index + 4 : index + 8])
        # print(year)
        if not (year >= 2020 and year <= 2030):
            # print("eyr {} is not between 2020 and 2030".format(year))
            continue

    if "hgt" in passport:
        index = passport.index("hgt")
        height = passport[index + 4 : index + 9]
        # print(height)
        if "cm" in height:
            height2 = int(height.split("cm")[0])
            if not (height2 >= 150 and height2 <= 193):
                # print("{} is not between 150cm and 193cm".format(height))
                continue
        elif "in" in height:
            height2 = int(height.split("in")[0])
            if not (height2 >= 59 and height2 <= 76):
                # print("{} is not between 59in and 76in".format(height))
                continue
        else:
            continue

    if "hcl" in passport:
        index = passport.index("hcl")
        if passport[index + 4] != "#":
            continue
        color = passport[index + 5 : index + 11]
        # print(color)
        for char in color:
            if char not in hex_char:
                valid = False
                # print("{} in {} is not a valid hex character".format(char, color))
                continue
    if not valid:
        continue

    if "ecl" in passport:
        index = passport.index("ecl")
        color = passport[index + 4 : index + 7]
        # print(color)
        if color not in eye_col:
            # print("{} is not a valid eye_col".format(color))
            continue

    if "pid" in passport:
        pid_re = re.compile(r"pid:(\d*)")
        pass_id = pid_re.search(passport)[1]
        # print(pass_id)
        if not (pass_id.isnumeric() and len(pass_id) == 9):
            #print("{} is either not numeric or not 9 numbers long".format(pass_id))
            continue
    count += 1
print("Part Two : " + str(count))
