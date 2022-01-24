import pytest
from adventofcode.year_2015.day_06_2015 import part_one
from adventofcode.year_2015.day_06_2015 import part_two


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("turn on 0,0 through 999,999", 1000000),
        ("toggle 0,0 through 999,0", 1000),
        ("turn off 499,499 through 500,500", 0),
    ],
)
def test_part_one(line, expected):
    assert expected == part_one([line])


@pytest.mark.parametrize(
    ["line", "expected"],
    [("turn on 0,0 through 0,0", 1), ("toggle 0,0 through 999,999", 2000000)],
)
def test_part_two(line, expected):
    assert expected == part_two([line])
