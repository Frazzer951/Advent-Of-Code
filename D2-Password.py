num_valid = 0

with open("Day_2_input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        parts = line.split()

        min_max = parts[0].split("-")
        min_n = int(min_max[0])
        max_n = int(min_max[1])
        char = parts[1][0]
        string = parts[2]

        count = string.count(char)
        if count >= min_n and count <= max_n:
            num_valid += 1

print(num_valid)
