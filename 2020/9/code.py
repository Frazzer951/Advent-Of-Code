# Advent of code Year 2020 Day 9 solution
# Author = Frazzer951
# Date = December 2020

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def xmas_exploit(number_list, preamble_len=25):
    pos = preamble_len
    while pos != len(number_list):
        valid = False
        cur_num = int(number_list[pos])
        for i in range(pos - preamble_len, pos):
            for j in range(pos - preamble_len, pos):
                num_i = int(number_list[i])
                num_j = int(number_list[j])
                if num_i == num_j:
                    continue
                if num_i + num_j == cur_num:
                    valid = True
        if not valid:
            return cur_num
        pos += 1


test_input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split(
    "\n"
)

print("Test Input : " + str(xmas_exploit(test_input, 5)))

print("Part One : " + str(xmas_exploit(input)))


def find_set(number_list, num):
    for i in range(len(number_list)):
        num_set = [int(number_list[i])]
        num_sum = int(number_list[i])
        for j in range(i + 1, len(number_list)):
            j_num = int(number_list[j])
            num_sum += j_num
            if num_sum > num:
                continue
            num_set.append(j_num)
            if num_sum == num:
                return num_set


def part_2(number_list, preamble_len=25):
    num = xmas_exploit(number_list, preamble_len)
    num_set = find_set(number_list, num)
    min_num = min(num_set)
    max_num = max(num_set)
    return min_num + max_num


print("Test Input : " + str(part_2(test_input, 5)))

print("Part Two : " + str(part_2(input)))
