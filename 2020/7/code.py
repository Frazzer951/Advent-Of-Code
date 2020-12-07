# Advent of code Year 2020 Day 7 solution
# Author = Frazzer951
# Date = December 2020


class Bag:
    def __init__(self, color, contains):
        self.color = color
        self.contains = contains
        self.leads_to_gold = False

        self.contents = self.get_contents()

    def get_contents(self):
        contents = {}

        if "no other bags" in self.contains:
            return contents

        for content in self.contains:
            num, color = content.split(" ", 1)
            color = color.rsplit(" ", 1)[0]
            # print('num: {}, color: {}'.format(num, color))
            contents[color] = int(num)
            if color == "shiny gold":
                self.leads_to_gold = True

        return contents


with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.readlines()


def make_bags(rules, bags):
    for rule in rules:
        rule = rule.strip()
        bag_color, contents = rule.split(" contain ")
        bag_color = bag_color.rsplit(" ", 1)[0]
        contents = contents.strip(".").split(", ")
        bags[bag_color] = Bag(bag_color, contents)


def count_shiny_gold(bags):
    main_count = 0
    while True:
        for bag in bags:
            for inner_bag in bags[bag].contents:
                if bags[inner_bag].leads_to_gold:
                    bags[bag].leads_to_gold = True
        count = 0
        for bag in bags:
            if bags[bag].leads_to_gold:
                count += 1

        if count == main_count:
            break
        else:
            main_count = count
    return main_count


test_input = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags.",
]

test_bags = {}
make_bags(test_input, test_bags)

print("Test Input : " + str(count_shiny_gold(test_bags)))

bags = {}
make_bags(input, bags)

print("Part One : " + str(count_shiny_gold(bags)))


print("Part Two : " + str(None))
