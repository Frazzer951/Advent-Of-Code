import pytest
from adventofcode.year_2015.day_09_2015 import part_one, part_two


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        (
            [
                "London to Dublin = 464",
                "London to Belfast = 518",
                "Dublin to Belfast = 141",
            ],
            605,
        )
    ],
)
def test_part_one(line, expected):
    assert expected == part_one(line)


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        (
            [
                "London to Dublin = 464",
                "London to Belfast = 518",
                "Dublin to Belfast = 141",
            ],
            804,
        )
    ],
)
def test_part_two(line, expected):
    assert expected == part_two([line])
