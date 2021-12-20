import pytest
from adventofcode.year_2020.day_05_2020 import get_seat_from_code


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("FBFBBFFRLR", 357),
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119),
        ("BBFFBBFRLL", 820),
    ],
)
def test_get_seat_from_code(line, expected):
    assert expected == get_seat_from_code(line)
