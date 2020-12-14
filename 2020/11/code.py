# Advent of code Year 2020 Day 11 solution
# Author = Frazzer951
# Date = December 2020

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def string_to_char(data):
    new_list = []
    for line in data:
        new_line = []
        for char in line:
            new_line.append(char)
        new_list.append(new_line)
    return new_list


def copy(state):
    new_state = []
    for line in state:
        new_line = []
        for char in line:
            new_line.append(char)
        new_state.append(new_line)
    return new_state


def get_state(x, y, state):
    num_neighbors = 0
    for x_pos in range(x - 1, x + 2):
        if x_pos < 0:
            continue
        if x_pos >= len(state):
            continue
        for y_pos in range(y - 1, y + 2):
            if y_pos < 0:
                continue
            if y_pos >= len(state[x]):
                continue
            if x_pos == x and y_pos == y:
                continue
            if state[x_pos][y_pos] == "#":
                num_neighbors += 1
    if num_neighbors == 0:
        return "#"
    if state[x][y] == "#" and num_neighbors >= 4:
        return "L"
    return state[x][y]


def next_state(state):
    new_state = copy(state)
    for x in range(len(state)):
        for y in range(len(state[x])):
            if state[x][y] == ".":
                continue
            new_state[x][y] = get_state(x, y, state)
    return new_state


def get_count(state):
    count = 0
    for line in state:
        for char in line:
            if char == "#":
                count += 1
    return count


def render(data):
    for line in data:
        string = ""
        for char in line:
            string += char
        print(string)


def final_seat_count(state):
    while True:
        old_state = copy(state)
        state = next_state(state)

        if old_state == state:
            break
    return get_count(state)


test_input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".split(
    "\n"
)
test_input = string_to_char(test_input)

print("Test Input : " + str(final_seat_count(test_input)))

input = string_to_char(input)
print("Part One : " + str(final_seat_count(input)))


print("Part Two : " + str(None))
