# Advent of code Year 2020 Day 6 solution
# Author = Frazzer951
# Date = December 2020

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.readlines()


def question_counter(group_answer):
    groups = []
    string = ""
    for line in group_answer:
        if line == "\n":
            groups.append(string)
            string = ""
        else:
            for char in line.strip("\n"):
                if char not in string:
                    string += char
    groups.append(string)
    # print(groups)
    count = 0
    for group in groups:
        count += len(group)
    return count


test_input = [
    "abc",
    "\n",
    "a",
    "b",
    "c",
    "\n",
    "ab",
    "ac",
    "\n",
    "a",
    "a",
    "a",
    "a",
    "\n",
    "b",
]

print("Test Input 1: " + str(question_counter(test_input)))
print("Part One : " + str(question_counter(input)))


def question_counter_all_answer(group_answer):
    groups = []
    string = ""
    first_line = True
    for line in group_answer:
        if line == "\n":
            groups.append(string)
            string = ""
            first_line = True
        else:
            if first_line:
                string = line.strip("\n")
                first_line = False
                continue
            new_string = ""
            for char in line.strip("\n"):
                if char in string:
                    new_string += char
            string = new_string
    groups.append(string)
    # print(groups)
    count = 0
    for group in groups:
        count += len(group)
    return count


print("Test Input 1: " + str(question_counter_all_answer(test_input)))
print("Part Two : " + str(question_counter_all_answer(input)))
