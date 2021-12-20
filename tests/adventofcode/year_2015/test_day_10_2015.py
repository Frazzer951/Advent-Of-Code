import pytest
from adventofcode.year_2015.day_10_2015 import lookAndSay


@pytest.mark.parametrize(
    ["line", "expected"],
    [("1", "11"), ("11", "21"), ("21", "1211"), ("1211", "111221")],
)
def test_lookAndSay(line, expected):
    assert expected == lookAndSay(line)
