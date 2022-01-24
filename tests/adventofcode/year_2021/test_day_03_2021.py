from adventofcode.year_2021.day_03_2021 import part_one
from adventofcode.year_2021.day_03_2021 import part_two


def test_part_one():
    assert 198 == part_one(
        [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
    )


def test_part_two():
    assert 230 == part_two(
        [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
    )
