from adventofcode.year_2020.day_06_2020 import part_one
from adventofcode.year_2020.day_06_2020 import part_two


def test_part_one():
    assert 11 == part_one(
        [
            "abc",
            "",
            "a",
            "b",
            "c",
            "",
            "ab",
            "ac",
            "",
            "a",
            "a",
            "a",
            "a",
            "",
            "b",
        ]
    )


def test_part_two():
    assert 6 == part_two(
        [
            "abc",
            "",
            "a",
            "b",
            "c",
            "",
            "ab",
            "ac",
            "",
            "a",
            "a",
            "a",
            "a",
            "",
            "b",
        ]
    )
