import pytest
from adventofcode.year_2015.day_17_2015 import find_combinations, part_two


def test_part_one():
    assert 150 == find_combinations(["20", "15", "10", "5", "5"], 25)


@pytest.mark.parametrize(["line", "expected"], [("", "")])
def test_part_two(line, expected):
    assert expected == part_two(line)
