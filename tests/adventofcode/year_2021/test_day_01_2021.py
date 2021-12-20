import pytest
from adventofcode.year_2021.day_01_2021 import part_one, part_two


@pytest.mark.parametrize(["line", "expected"], [([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 7)])
def test_part_one(line, expected):
    assert expected == part_one(line)


@pytest.mark.parametrize(["line", "expected"], [([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 5)])
def test_part_two(line, expected):
    assert expected == part_two(line)
