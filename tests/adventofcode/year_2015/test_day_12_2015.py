import pytest
from adventofcode.year_2015.day_12_2015 import part_one
from adventofcode.year_2015.day_12_2015 import part_two


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("[1, 2, 3]", 6),
        ('{"a": 2, "b": 4}', 6),
        ("[[[3]]]", 3),
        ('{"a": {"b": 4}, "c": -1}', 3),
        ('{"a": [-1, 1]}', 0),
        ('[-1, {"a": 1}]', 0),
        ("[]", 0),
        ("[]", 0),
    ],
)
def test_part_one(line, expected):
    assert expected == part_one([line])


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("[1, 2, 3]", 6),
        ('[1,{"c":"red","b":2},3]', 4),
        ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
        ('[1,"red",5] ', 6),
    ],
)
def test_part_two(line, expected):
    assert expected == part_two([line])
