import pytest
from adventofcode.year_2021.day_02_2021 import part_one, part_two


@pytest.mark.parametrize(["line", "expected"], [(["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"], 150)])
def test_part_one(line, expected):
    assert expected == part_one(line)


@pytest.mark.parametrize(["line", "expected"], [(["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"], 900)])
def test_part_two(line, expected):
    assert expected == part_two(line)
