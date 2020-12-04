# Generate Map
# Check x,y coordinate for tree
# keep checking until you reach the bottom


with open("Day_3_Input.txt", "r") as f:
    map = f.readlines()

width = len(map[0]) - 1
bottom = len(map) - 1


def check_tree(x, y, print_map):
    x = x % width
    tree = map[y][x] == "#"
    if print_map:
        string = ""
        for i in range(width):
            if i == x and tree:
                string += "X"
            elif i == x and not tree:
                string += "O"
            else:
                string += map[y][i]
        print(string)
    return tree


def check_slope(x_mod, y_mod, print_map=False):
    count = 0
    pos_x, pos_y = (0, 0)
    while pos_y <= bottom:
        if check_tree(pos_x, pos_y, print_map):
            count += 1
        pos_x += x_mod
        pos_y += y_mod

    print(
        "With a slope of Right {}, Down {}, you hit {} trees".format(
            x_mod, y_mod, count
        )
    )
    return count


s1 = check_slope(1, 1)
s2 = check_slope(3, 1) # Part one answer
s3 = check_slope(5, 1)
s4 = check_slope(7, 1)
s5 = check_slope(1, 2)

prod = s1 * s2 * s3 * s4 * s5 # Part two answer

print("{}*{}*{}*{}*{}={}".format(s1, s2, s3, s4, s5, prod))
