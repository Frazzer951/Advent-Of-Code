import pytest
from adventofcode.year_2020.day_01_2020 import part_one
from adventofcode.year_2020.day_01_2020 import part_two


@pytest.mark.parametrize(["line", "expected"], [([1721, 979, 366, 299, 675, 1456], 514579)])
def test_part_one(line, expected):
    assert expected == part_one(line)


@pytest.mark.parametrize(["line", "expected"], [([1721, 979, 366, 299, 675, 1456], 241861950)])
def test_part_two(line, expected):
    assert expected == part_two(line)
