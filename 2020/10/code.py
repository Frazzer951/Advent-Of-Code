# Advent of code Year 2020 Day 10 solution
# Author = Frazzer951
# Date = December 2020

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")

num_input = []
for line in input:
    num_input.append(int(line))


def count_differences(data):
    data.sort()
    diff_count = {1: 0, 3: 1}
    diff_count[data[0]] += 1
    for i in range(1, len(data)):
        diff = data[i] - data[i - 1]
        diff_count[diff] += 1

    return diff_count


test_input = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
test_input2 = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3,
]

print("Test input: " + str(count_differences(test_input)))
print("Test input2: " + str(count_differences(test_input2)))

diff_count = count_differences(num_input)
print("Part One : " + str(diff_count[1] * diff_count[3]))


def count_permutation(data, cur_node=0):
    # for each node, look at the possible next nodes
    data.sort()
    possible_nodes = []
    for node in data:
        if node <= cur_node:
            continue
        if node - 3 > cur_node:
            break
        possible_nodes.append(node)
    count = 0
    for node in possible_nodes:
        count += count_permutation(data, node)
    return len(possible_nodes) + count


# count_permutation(test_input)
print("Test input : " + str(count_permutation(test_input)))
print("Part Two : " + str(None))
