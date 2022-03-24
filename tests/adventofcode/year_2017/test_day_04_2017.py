import pytest
from adventofcode.year_2017.day_04_2017 import is_valid_passphrase
from adventofcode.year_2017.day_04_2017 import is_valid_passphrase_2


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("aa bb cc dd ee", True),
        ("aa bb cc dd aa", False),
        ("aa bb cc dd aaa", True),
    ],
)
def test_part_one(line, expected):
    assert expected == is_valid_passphrase(line)


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("abcde fghij", True),
        ("abcde xyz ecdab", False),
        ("a ab abc abd abf abj", True),
        ("iiii oiii ooii oooi oooo", True),
        ("oiii ioii iioi iiio", False),
    ],
)
def test_part_two(line, expected):
    assert expected == is_valid_passphrase_2(line)
