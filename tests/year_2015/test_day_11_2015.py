import pytest
from adventofcode.year_2015.day_11_2015 import is_valid


@pytest.mark.parametrize(
    ["line", "expected"],
    [("hijklmmn", False), ("abbceffg", False), ("abbcegjk", False)],
)
def test_is_valid(line, expected):
    assert expected == is_valid(line)
