import pytest
from adventofcode.year_2015.day_25_2015 import getCode


@pytest.mark.parametrize(["x", "y", "expected"], [(1, 1, 20151125), (2, 1, 31916031), (5, 3, 28094349)])
def test_part_one(x, y, expected):
    assert expected == getCode(x, y)
