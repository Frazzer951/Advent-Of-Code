# Advent of code Year 2020 Day 8 solution
# Author = Frazzer951
# Date = December 2020

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def compile(commands):
    visited = []
    size = len(commands)
    line_number = 0
    acc = 0
    while line_number not in visited and line_number != size:
        command, value = commands[line_number]
        value = int(value)
        # print('Command: {}, Value: {}'.format(command, value))
        if command == "nop":
            visited.append(line_number)
            line_number += 1
        if command == "jmp":
            visited.append(line_number)
            line_number += value
        if command == "acc":
            visited.append(line_number)
            acc += value
            line_number += 1
    return acc, line_number


def com_val_split(commands):
    command_and_value = []
    for command in commands:
        command_and_value.append(command.split())
    return command_and_value


test_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".split(
    "\n"
)
test_input = com_val_split(test_input)


print("Test Input : " + str((compile(test_input)[0])))

input = com_val_split(input)

print("Part One : " + str(compile(input)[0]))


def part_2(commands):
    for i in range(len(commands)):
        if commands[i][0] == "jmp":
            commands[i][0] = "nop"
            acc, line_num = compile(commands)
            commands[i][0] = "jmp"
        elif commands[i][0] == "nop":
            commands[i][0] = "jmp"
            acc, line_num = compile(commands)
            commands[i][0] = "nop"
        else:
            continue

        if line_num == len(commands):
            return acc


print("Test Input : " + str(part_2(test_input)))


print("Part Two : " + str(part_2(input)))
