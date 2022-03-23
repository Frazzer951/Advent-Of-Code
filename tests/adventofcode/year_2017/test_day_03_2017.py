import pytest
from adventofcode.year_2017.day_03_2017 import part_one
from adventofcode.year_2017.day_03_2017 import part_two


@pytest.mark.parametrize(["line", "expected"], [(["1"], 0), (["12"], 3), (["23"], 2), (["1024"], 31)])
def test_part_one(line, expected):
    assert expected == part_one(line)


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        (["1"], 2),
        (["2"], 4),
        (["4"], 5),
        (["5"], 10),
        (["133"], 142),
    ],
)
def test_part_two(line, expected):
    assert expected == part_two(line)
