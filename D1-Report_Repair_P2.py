numbers = []

with open("Day_1_input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        numbers.append(int(line))

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        for k in range(j, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                print(
                    "{num1}+{num2}+{num3}=2020: {num1}*{num2}*{num3}={num4}".format(
                        num1=numbers[i], num2=numbers[j], num3=numbers[k], num4=numbers[i] * numbers[j]*numbers[k]
                    )
            )
