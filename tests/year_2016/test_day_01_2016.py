import pytest
from adventofcode.year_2016.day_01_2016 import numBlocksAway_1, numBlocksAway_2


@pytest.mark.parametrize(
    ["line", "expected"],
    [(["R2", "L3"], 5), (["R2", "R2", "R2"], 2), (["R5", "L5", "R5", "R3"], 12)],
)
def test_numBlocksAway_1(line, expected):
    assert expected == numBlocksAway_1(line)


@pytest.mark.parametrize(["line", "expected"], [(["R8", "R4", "R4", "R8"], 4)])
def test_numBlocksAway_2(line, expected):
    assert expected == numBlocksAway_2(line)
