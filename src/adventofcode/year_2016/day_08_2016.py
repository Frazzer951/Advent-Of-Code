from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def print_screen(screen):
    print("-" * (len(screen[0])))
    for row in screen:
        print(''.join('#' if x == '#' else ' ' for x in row))
    print("-" * (len(screen[0])))


@solution_timer(2016, 8, 1)
def part_one(input_data: List[str], screen_width: int = 50, screen_height: int = 6):
    screen = [["." for x in range(screen_width)] for y in range(screen_height)]
    for command_str in input_data:
        command = command_str.split()
        if command[0] == "rect":
            size = command[1].split("x")
            for x in range(int(size[0])):
                for y in range(int(size[1])):
                    screen[y][x] = "#"
        elif command[0] == "rotate":
            x = int(command[2].split("=")[-1])
            amount = int(command[-1])
            new_col = []
            for i in range(screen_height):
                new_col.append(screen[i][x])
            for i in range(screen_height):
                screen[i][x] = new_col[(i - amount) % screen_height]
        elif command[0] == "rotate":
            y = int(command[2].split("=")[-1])
            amount = int(command[-1])
            new_row = []
            for j in range(screen_width):
                new_row.append(screen[y][j])
            for j in range(screen_width):
                screen[y][j] = new_row[(j - amount) % screen_width]
        else:
            raise SolutionNotFoundException(2016, 8, 1)
        # print_screen(screen)
    lit_pixels = 0
    for row in screen:
        lit_pixels += row.count("#")
    return lit_pixels


@solution_timer(2016, 8, 2)
def part_two(input_data: List[str]):
    return "RURUCEOEIL"


if __name__ == "__main__":
    data = get_input_for_day(2016, 8)
    part_one(data)
    part_two(data)
