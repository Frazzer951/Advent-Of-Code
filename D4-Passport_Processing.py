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
            print("Not Valid, {} not in string {}".format(req, passport))
            continue
    if valid:
        count += 1

print(len(passports))
print(count)