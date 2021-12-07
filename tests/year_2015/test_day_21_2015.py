import pytest
from adventofcode.year_2015.day_21_2015 import stats, simFight


@pytest.mark.parametrize(
    ["player", "boss", "expected"], [(stats(8, 5, 5), stats(12, 7, 2), True), (stats(100, 6, 0), stats(109, 8, 2), False)]
)
def test_part_one(player, boss, expected):
    assert expected == simFight(player, boss)
