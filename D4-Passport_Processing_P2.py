import re

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

with open("Day_4_Input.txt", "r") as f:
    lines = f.readlines()
    string = ""
    for line in lines:
        if line == "\n":
            passports.append(string)
            # print(string)
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
            continue

    if not valid:
        continue

    if "byr" in passport:
        index = passport.index("byr")
        year = int(passport[index + 4 : index + 8])
        # print(year)
        if not (year >= 1920 and year <= 2002):
            #print("byr {} is not between 1920 and 2002".format(year))
            continue

    if "iyr" in passport:
        index = passport.index("iyr")
        year = int(passport[index + 4 : index + 8])
        # print(year)
        if not (year >= 2010 and year <= 2020):
            #print("iyr {} is not between 2010 and 2020".format(year))
            continue

    if "eyr" in passport:
        index = passport.index("eyr")
        year = int(passport[index + 4 : index + 8])
        # print(year)
        if not (year >= 2020 and year <= 2030):
            #print("eyr {} is not between 2020 and 2030".format(year))
            continue

    if "hgt" in passport:
        index = passport.index("hgt")
        height = passport[index + 4 : index + 9]
        #print(height)
        if "cm" in height:
            height2 = int(height.split("cm")[0])
            if not (height2 >= 150 and height2 <= 193):
                #print("{} is not between 150cm and 193cm".format(height))
                continue
        elif "in" in height:
            height2 = int(height.split("in")[0])
            if not (height2 >= 59 and height2 <= 76):
                #print("{} is not between 59in and 76in".format(height))
                continue
        else:
            continue

    if "hcl" in passport:
        index = passport.index("hcl")
        if passport[index + 4] != "#":
            continue
        color = passport[index + 5 : index + 11]
        #print(color)
        for char in color:
            if char not in hex_char:
                valid = False
                #print("{} in {} is not a valid hex character".format(char, color))
                continue
    if not valid:
        continue

    if "ecl" in passport:
        index = passport.index("ecl")
        color = passport[index + 4 : index + 7]
        # print(color)
        if color not in eye_col:
            #print("{} is not a valid eye_col".format(color))
            continue

    if "pid" in passport:
        pid_re = re.compile(r'pid:(\d*)')
        pass_id = pid_re.search(passport)[1]
        # print(pass_id)
        if not (pass_id.isnumeric() and len(pass_id) == 9):
            print("{} is either not numeric or not 9 numbers long".format(pass_id))
            continue
    count += 1

"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""

print("The Number of Valid Passports is {}".format(count))
