import pytest
from adventofcode.year_2017.day_01_2017 import part_one
from adventofcode.year_2017.day_01_2017 import part_two


@pytest.mark.parametrize(["line", "expected"], [("1122", 3), ("1111", 4), ("1234", 0), ("91212129", 9)])
def test_part_one(line, expected):
    assert expected == part_one([line])


@pytest.mark.parametrize(["line", "expected"], [("1212", 6), ("1221", 0), ("123425", 4), ("123123", 12), ("12131415", 4)])
def test_part_two(line, expected):
    assert expected == part_two([line])
