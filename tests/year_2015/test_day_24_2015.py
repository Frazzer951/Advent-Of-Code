import pytest
from adventofcode.year_2015.day_24_2015 import part_one, part_two


@pytest.mark.parametrize(
    ["line", "expected"], [("","")]
)
def test_part_one(line, expected):
    assert expected == part_one(line)


@pytest.mark.parametrize(
    ["line", "expected"], [("","")]
)
def test_part_two(line, expected):
    assert expected == part_two(line)
