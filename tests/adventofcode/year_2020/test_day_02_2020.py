import pytest
from adventofcode.year_2020.day_02_2020 import (
    part_one,
    part_two,
    is_valid_password_1,
    is_valid_password_2,
)


@pytest.mark.parametrize(
    ["line", "expected"],
    [("1-3 a: abcde", True), ("1-3 b: cdefg", False), ("2-9 c: ccccccccc", True)],
)
def test_is_valid_password_1(line, expected):
    assert expected == is_valid_password_1(line)


def test_part_one():
    assert 2 == part_one(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"])


@pytest.mark.parametrize(
    ["line", "expected"],
    [("1-3 a: abcde", True), ("1-3 b: cdefg", False), ("2-9 c: ccccccccc", False)],
)
def test_is_valid_password_2(line, expected):
    assert expected == is_valid_password_2(line)


def test_part_two():
    assert 1 == part_two(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"])
