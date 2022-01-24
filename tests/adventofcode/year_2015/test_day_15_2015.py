from adventofcode.year_2015.day_15_2015 import part_one
from adventofcode.year_2015.day_15_2015 import part_two


def test_part_one():
    assert 62842880 == part_one(
        [
            "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
            "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
        ]
    )


def test_part_two():
    assert 57600000 == part_two(
        [
            "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
            "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
        ]
    )
