# Advent of code Year 2015 Day 21 solution
# Author = Frazzer951
# Date = October 2021

from dataclasses import dataclass
import math

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


@dataclass
class stats:
    hp: int
    dmg: int
    armor: int


def simFight(player, boss):
    while player.hp > 0 and boss.hp > 0:
        boss.hp -= max(1, player.dmg - boss.armor)
        if boss.hp <= 0:
            return True
        player.hp -= max(1, boss.dmg - player.armor)
    return False


player = stats(8, 5, 5)
boss = stats(12, 7, 2)
t1 = simFight(player, boss)
assert t1 == True

player = stats(100, 6, 0)
boss = stats(109, 8, 2)
t2 = simFight(player, boss)
assert t2 == False


def CoinsNeeded(bossStats):
    weapons = {
        "Dagger": [8, 4, 0],
        "Shortsword": [10, 5, 0],
        "Warhammer": [25, 6, 0],
        "Longsword": [40, 7, 0],
        "Greataxe": [74, 8, 0],
    }
    armors = {
        "None": [0, 0, 0],
        "Leather": [13, 0, 1],
        "Chainmail": [31, 0, 2],
        "Splintmail": [53, 0, 3],
        "Bandedmail": [75, 0, 4],
        "Platemail": [102, 0, 5],
    }
    rings = {
        "None": [0, 0, 0],
        "Damage +1": [25, 1, 0],
        "Damage +2": [50, 2, 0],
        "Damage +3": [100, 3, 0],
        "Defense +1": [20, 0, 1],
        "Defense +2": [40, 0, 2],
        "Defense +3": [80, 0, 3],
    }

    # Generate all possible combinations of items
    minCost = math.inf
    maxCost = -math.inf
    for weapon in weapons:
        for armor in armors:
            for ring1 in rings:
                for ring2 in rings:
                    if ring1 == ring2 and ring1 != "None":
                        continue
                    # Simulate fight
                    cost = (
                        weapons[weapon][0]
                        + armors[armor][0]
                        + rings[ring1][0]
                        + rings[ring2][0]
                    )
                    player = stats(
                        100,
                        weapons[weapon][1] + rings[ring1][1] + rings[ring2][1],
                        armors[armor][2] + rings[ring1][2] + rings[ring2][2],
                    )
                    boss = stats(
                        bossStats.hp,
                        bossStats.dmg,
                        bossStats.armor,
                    )
                    if simFight(player, boss):
                        minCost = min(minCost, cost)
                    else:
                        maxCost = max(maxCost, cost)
    return minCost, maxCost


boss = stats(109, 8, 2)
coins = CoinsNeeded(boss)
print(f"Min Coins needed to win: {coins[0]}")
print(f"Max Coins and still loose: {coins[1]}")
