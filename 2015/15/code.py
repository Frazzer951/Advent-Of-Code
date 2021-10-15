# Advent of code Year 2015 Day 15 solution
# Author = Frazzer951
# Date = October 2021

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)


class Recipe:
    def __init__(self):
        self.capacity = 0
        self.durability = 0
        self.flavor = 0
        self.texture = 0
        self.calories = 0

    def get_score(self):
        return (
            max(self.capacity, 0)
            * max(self.durability, 0)
            * max(self.flavor, 0)
            * max(self.texture, 0)
        )

    def add_ingredient(self, ingredient, amount=1):
        self.capacity += ingredient.capacity * amount
        self.durability += ingredient.durability * amount
        self.flavor += ingredient.flavor * amount
        self.texture += ingredient.texture * amount
        self.calories += ingredient.calories * amount


def multichoose(n, k):
    if not k:
        return [[0] * n]
    if not n:
        return []
    if n == 1:
        return [[k]]
    return [[0] + val for val in multichoose(n - 1, k)] + [
        [val[0] + 1] + val[1:] for val in multichoose(n, k - 1)
    ]


def part1(input):
    ingredients = []
    for line in input:
        split_line = line.split()
        ingredients.append(
            Ingredient(
                split_line[0][:-1],  # Name
                split_line[2][:-1],  # Capacity
                split_line[4][:-1],  # Durability
                split_line[6][:-1],  # Flavor
                split_line[8][:-1],  # Texture
                split_line[10],  # Calories
            )
        )

    counts = multichoose(len(ingredients), 100)
    maxScore = 0

    for count in counts:
        r = Recipe()
        for i in range(len(ingredients)):
            r.add_ingredient(ingredients[i], count[i])
        maxScore = max(maxScore, r.get_score())

    return maxScore


t1 = part1(
    [
        "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
        "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
    ]
)
print("Part One Test 1: " + str(t1))

p1 = part1(input)
print("Part One : " + str(p1))


def part2(input):
    ingredients = []
    for line in input:
        split_line = line.split()
        ingredients.append(
            Ingredient(
                split_line[0][:-1],  # Name
                split_line[2][:-1],  # Capacity
                split_line[4][:-1],  # Durability
                split_line[6][:-1],  # Flavor
                split_line[8][:-1],  # Texture
                split_line[10],  # Calories
            )
        )

    counts = multichoose(len(ingredients), 100)
    maxScore = 0

    for count in counts:
        r = Recipe()
        for i in range(len(ingredients)):
            r.add_ingredient(ingredients[i], count[i])
        if r.calories == 500:
            maxScore = max(maxScore, r.get_score())

    return maxScore


t3 = part2(
    [
        "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
        "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
    ]
)
print("Part Two Test 1: " + str(t3))

p2 = part2(input)
print("Part Two : " + str(p2))