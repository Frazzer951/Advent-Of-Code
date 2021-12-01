from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def parse_passports(passports: List[str]):
    passport = ''
    for line in passports:
        if line == '':
            if passport != '':
                yield passport
            passport = ''
        else:
            passport += line + ' '
    if passport != '':
        yield passport


def verify_passport_1(passport: str):
    fields = passport.split()
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    passport = {field.split(':')[0]: field.split(':')[1] for field in fields}
    for field in required_fields:
        if field not in passport:
            return False
    return True


def verify_passport_2(passport: str):
    fields = passport.split()
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    passport = {field.split(':')[0]: field.split(':')[1] for field in fields}
    for field in required_fields:
        if field not in passport:
            return False
    if not (1920 <= int(passport['byr']) <= 2002):
        return False
    if not (2010 <= int(passport['iyr']) <= 2020):
        return False
    if not (2020 <= int(passport['eyr']) <= 2030):
        return False
    if passport['hgt'][-2:] == 'cm':
        if not (150 <= int(passport['hgt'][:-2]) <= 193):
            return False
    if passport['hgt'][-2:] == 'in':
        if not (59 <= int(passport['hgt'][:-2]) <= 76):
            return False
    if passport['hcl'][0] != '#':
        return False
    if len(passport['hcl'][1:]) != 6:
        return False
    for c in passport['hcl'][1:]:
        if c not in '0123456789abcdef':
            return False
    if passport['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        return False
    if not (len(passport['pid']) == 9 and passport['pid'].isdigit()):
        return False
    return True


@solution_timer(2020, 4, 1)
def part_one(input_data: List[str]):
    valid = 0
    for passport in parse_passports(input_data):
        if verify_passport_1(passport):
            valid += 1
    return valid


@solution_timer(2020, 4, 2)
def part_two(input_data: List[str]):
    valid = 0
    for passport in parse_passports(input_data):
        if verify_passport_2(passport):
            valid += 1
    return valid


if __name__ == "__main__":
    data = get_input_for_day(2020, 4)
    part_one(data)
    part_two(data)
