numbers = []

with open("Day_1_input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        numbers.append(int(line))

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if numbers[i] + numbers[j] == 2020:
            print(
                "{num1}+{num2}=2020: {num1}*{num2}={num3}".format(
                    num1=numbers[i], num2=numbers[j], num3=numbers[i] * numbers[j]
                )
            )
