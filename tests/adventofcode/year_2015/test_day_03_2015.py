import pytest
from adventofcode.year_2015.day_03_2015 import part_one, part_two


@pytest.mark.parametrize(["line", "expected"], [(">", 2), ("^>v<", 4), ("^v^v^v^v^v", 2)])
def test_part_one(line, expected):
    assert expected == part_one([line])


@pytest.mark.parametrize(["line", "expected"], [("^v", 3), ("^>v<", 3), ("^v^v^v^v^v", 11)])
def test_part_two(line, expected):
    assert expected == part_two([line])
