# Advent of code Year 2015 Day 23 solution
# Author = Frazzer951
# Date = October 2021

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def sim_code(input, registers={"a": 0, "b": 0}):
    ip = 0
    while ip < len(input):
        line = input[ip].split()
        if line[0] == "hlf":
            reg = line[1]
            registers[reg] = registers[reg] // 2
        elif line[0] == "tpl":
            reg = line[1]
            registers[reg] = registers[reg] * 3
        elif line[0] == "inc":
            reg = line[1]
            registers[reg] += 1
        elif line[0] == "jmp":
            ip += int(line[1])
            continue
        elif line[0] == "jie":
            reg = line[1].strip(",")
            if registers[reg] % 2 == 0:
                ip += int(line[2])
                continue
        elif line[0] == "jio":
            reg = line[1].strip(",")
            if registers[reg] == 1:
                ip += int(line[2])
                continue
        ip += 1
    return registers


t1 = sim_code(
    [
        "inc a",
        "jio a, +2",
        "tpl a",
        "inc a  ",
    ]
)
print("Part One Test 1: " + str(t1))
assert t1["a"] == 2

p1 = sim_code(input)
print("Part One : " + str(p1))

p2 = sim_code(input, {"a": 1, "b": 0})
print("Part Two : " + str(p2))
