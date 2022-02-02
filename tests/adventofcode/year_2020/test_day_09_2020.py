from adventofcode.year_2020.day_09_2020 import part_one
from adventofcode.year_2020.day_09_2020 import part_two


def test_part_one():
    assert 127 == part_one(
        [
            "35",
            "20",
            "15",
            "25",
            "47",
            "40",
            "62",
            "55",
            "65",
            "95",
            "102",
            "117",
            "150",
            "182",
            "127",
            "219",
            "299",
            "277",
            "309",
            "576",
        ],
        5,
    )


def test_part_two():
    assert 62 == part_two(
        [
            "35",
            "20",
            "15",
            "25",
            "47",
            "40",
            "62",
            "55",
            "65",
            "95",
            "102",
            "117",
            "150",
            "182",
            "127",
            "219",
            "299",
            "277",
            "309",
            "576",
        ],
        5,
    )
