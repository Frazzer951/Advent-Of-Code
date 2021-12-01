import pytest
from adventofcode.year_2015.day_04_2015 import part_one


@pytest.mark.parametrize(
    ["line", "expected"], [("abcdef", 609043), ("pqrstuv", 1048970)]
)
def test_part_one(line, expected):
    assert expected == part_one([line])
