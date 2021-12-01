from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

import math

SPELL_COSTS = {
    "magic_missle": 53,
    "drain": 73,
    "shield": 113,
    "poison": 173,
    "recharge": 229,
}


def apply_effects(game):
    if game["shield_timer"]:
        game["shield_timer"] -= 1
        if game["shield_timer"] == 0:
            game["player_armor"] = 0
    if game["poison_timer"]:
        game["boss_hp"] -= 3
        game["poison_timer"] -= 1
    if game["recharge_timer"]:
        game["player_mana"] += 101
        game["recharge_timer"] -= 1


def player_turn(game, spell):
    if spell == "magic_missle":
        game["boss_hp"] -= 4
    elif spell == "drain":
        game["boss_hp"] -= 2
        game["player_hp"] += 2
    elif spell == "shield":
        game["player_armor"] = 7
        game["shield_timer"] = 6
    elif spell == "poison":
        game["poison_timer"] = 6
    elif spell == "recharge":
        game["recharge_timer"] = 5
    game["player_mana"] -= SPELL_COSTS[spell]


def boss_turn(game):
    dmg = max(1, game["boss_dmg"] - game["player_armor"])
    game["player_hp"] -= dmg


def check_for_endgame(game, min_mana_spent):
    if game["boss_hp"] <= 0:
        min_mana_spent = min(game["mana_spent"], min_mana_spent)
        return 1, min_mana_spent
    if game["player_hp"] <= 0:
        return 2, min_mana_spent
    return 0, min_mana_spent


def try_all_spells(game, min_mana_spent, new_games):
    castable_spells = [
        spell for spell, cost in SPELL_COSTS.items() if cost <= game["player_mana"]
    ]
    if game["shield_timer"] and "shield" in castable_spells:
        castable_spells.remove("shield")
    if game["poison_timer"] and "poison" in castable_spells:
        castable_spells.remove("poison")
    if game["recharge_timer"] and "recharge" in castable_spells:
        castable_spells.remove("recharge")

    for spell in castable_spells:
        sub_game = game.copy()
        sub_game["spells_cast"] = list(sub_game["spells_cast"]) + [spell]
        sub_game["mana_spent"] = sub_game["mana_spent"] + SPELL_COSTS[spell]

        player_turn(sub_game, spell)
        endgame, min_mana_spent = check_for_endgame(sub_game, min_mana_spent)
        if endgame:
            continue

        if sub_game["mana_spent"] > min_mana_spent:
            continue

        apply_effects(sub_game)
        endgame, min_mana_spent = check_for_endgame(sub_game, min_mana_spent)
        if endgame:
            continue

        boss_turn(sub_game)
        endgame, min_mana_spent = check_for_endgame(sub_game, min_mana_spent)
        if endgame:
            continue

        new_games.append(sub_game)
    return min_mana_spent


def try_all_games(games, min_mana_spent, part2):
    new_games = []
    for game in games:
        if part2:
            game["player_hp"] -= 1
        endgame, min_mana_spent = check_for_endgame(game, min_mana_spent)
        if endgame:
            continue

        apply_effects(game)
        endgame, min_mana_spent = check_for_endgame(game, min_mana_spent)
        if endgame:
            continue

        min_mana_spent = try_all_spells(game, min_mana_spent, new_games)

    return new_games, min_mana_spent


def find_minimal_mana(game, part2=False):
    min_mana_spent = math.inf
    games = [game]
    while len(games):
        games, min_mana_spent = try_all_games(games, min_mana_spent, part2)
    return min_mana_spent


@solution_timer(2015, 22, 1)
def part_one(input_data: List[str]):
    initial_game = {
        "player_hp": 50,
        "player_mana": 500,
        "player_armor": 0,
        "boss_hp": 71,
        "boss_dmg": 10,
        "shield_timer": 0,
        "poison_timer": 0,
        "recharge_timer": 0,
        "spells_cast": [],
        "mana_spent": 0,
    }
    return find_minimal_mana(initial_game.copy())


@solution_timer(2015, 22, 2)
def part_two(input_data: List[str]):
    initial_game = {
        "player_hp": 50,
        "player_mana": 500,
        "player_armor": 0,
        "boss_hp": 71,
        "boss_dmg": 10,
        "shield_timer": 0,
        "poison_timer": 0,
        "recharge_timer": 0,
        "spells_cast": [],
        "mana_spent": 0,
    }
    return find_minimal_mana(initial_game.copy(), True)


if __name__ == "__main__":
    data = get_input_for_day(2015, 22)
    part_one(data)
    part_two(data)
