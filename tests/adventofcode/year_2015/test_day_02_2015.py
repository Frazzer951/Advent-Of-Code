import pytest
from adventofcode.year_2015.day_02_2015 import part_one, part_two


@pytest.mark.parametrize(["line", "expected"], [("2x3x4", 58), ("1x1x10", 43)])
def test_part_one(line, expected):
    assert expected == part_one([line])


@pytest.mark.parametrize(["line", "expected"], [("2x3x4", 34), ("1x1x10", 14)])
def test_part_two(line, expected):
    assert expected == part_two([line])
