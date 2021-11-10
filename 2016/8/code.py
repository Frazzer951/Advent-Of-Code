# Advent of code Year 2016 Day 8 solution
# Author = Frazzer951
# Date = November 2021

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def print_screen(screen):
    print("-" * (len(screen[0])))
    for row in screen:
        print(''.join('#' if x == '#' else ' ' for x in row))
    print("-" * (len(screen[0])))


def part1(input, screen_width=50, screen_height=6):
    screen = [["." for x in range(screen_width)] for y in range(screen_height)]
    for command in input:
        print(command)
        match command.split():
            case ["rect",size]:
                size = size.split("x")
                for x in range(int(size[0])):
                    for y in range(int(size[1])):
                        screen[y][x] = "#"
                print(size)
            case ['rotate','column',x,'by',amount]:
                x = int(x.split("=")[-1])
                amount = int(amount)
                new_col = []
                for i in range(screen_height):
                    new_col.append(screen[i][x])
                for i in range(screen_height):
                    screen[i][x] = new_col[(i - amount) % screen_height]
            case ['rotate','row',y,'by',amount]:
                y = int(y.split("=")[-1])
                amount = int(amount)
                new_row = []
                for j in range(screen_width):
                    new_row.append(screen[y][j])
                for j in range(screen_width):
                    screen[y][j] = new_row[(j - amount) % screen_width]
            case _:
                raise NotImplementedError("Command not implemented")
        print_screen(screen)
    lit_pixels = 0
    for row in screen:
        lit_pixels += row.count("#")
    return lit_pixels


t1 = part1(
    [
        "rect 3x2",
        "rotate column x=1 by 1",
        "rotate row y=0 by 4",
        "rotate column x=1 by 1",
    ],
    7,
    3,
)
print("Part One Test 1: " + str(t1))
assert t1 == 6

p1 = part1(input)
print("Part One : " + str(p1))
