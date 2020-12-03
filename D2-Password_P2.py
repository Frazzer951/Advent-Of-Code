num_valid = 0

with open("Day_2_input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        parts = line.split()

        indexes = parts[0].split("-")
        index1 = int(indexes[0])
        index2 = int(indexes[1])
        char = parts[1][0]
        string = parts[2]

        if string[index1 - 1] == char and string[index2 - 1] != char:
            num_valid += 1
        elif string[index1 - 1] != char and string[index2 - 1] == char:
            num_valid += 1

print(num_valid)
