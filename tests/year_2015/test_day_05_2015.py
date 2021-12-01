import pytest
from adventofcode.year_2015.day_05_2015 import isNice_1, isNice_2


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("ugknbfddgicrmopn", True),
        ("aaa", True),
        ("jchzalrnumimnmhp", False),
        ("haegwjzuvuyypxyu", False),
        ("dvszwmarrgswjxmb", False),
    ],
)
def test_isNice_one(line, expected):
    assert expected == isNice_1([line])


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("qjhvhtzxzqqjkmpb", True),
        ("xxyxx", True),
        ("uurcxstgmygtbstg", False),
        ("ieodomkazucvgmuy", False),
    ],
)
def test_isNice_two(line, expected):
    assert expected == isNice_2([line])
