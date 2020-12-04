# Advent of code Year 2020 Day 1 solution
# Author = Frazzer951
# Date = December 2020

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.readlines()


numbers = []
for line in input:
    numbers.append(int(line))


for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if numbers[i] + numbers[j] == 2020:
            # print("{num1}+{num2}=2020: {num1}*{num2}={num3}".format(num1=numbers[i], num2=numbers[j], num3=numbers[i] * numbers[j]))
            p1_sol = numbers[i] * numbers[j]
print("Part One : " + str(p1_sol))


for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        for k in range(j, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                # print("{num1}+{num2}+{num3}=2020: {num1}*{num2}*{num3}={num4}".format(num1=numbers[i], num2=numbers[j], num3=numbers[k], num4=numbers[i] * numbers[j]*numbers[k]))
                p2_sol = numbers[i] * numbers[j] * numbers[k]
print("Part Two : " + str(p2_sol))
