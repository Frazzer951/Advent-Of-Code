import pytest
from adventofcode.year_2015.day_14_2015 import get_distance
from adventofcode.year_2015.day_14_2015 import part_two


@pytest.mark.parametrize(
    ["speed", "time", "rest", "seconds", "expected"], [(14, 10, 127, 1000, 1120), (16, 11, 162, 1000, 1056)]
)
def test_part_one(speed, time, rest, seconds, expected):
    assert expected == get_distance(speed, time, rest, seconds)


def test_part_two():
    assert 689 == part_two(
        [
            "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
            "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
        ],
        seconds=1000,
    )
