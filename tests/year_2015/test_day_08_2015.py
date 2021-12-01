import pytest
from adventofcode.year_2015.day_08_2015 import size_in_memory, size_encoded


@pytest.mark.parametrize(
    ["line", "expected"],
    [(r'""', 0), (r'"abc"', 3), (r'"aaa\"aaa"', 7), (r'"\x27"', 1)],
)
def test_size_in_memory(line, expected):
    assert expected == size_in_memory(line)


@pytest.mark.parametrize(
    ["line", "expected"],
    [(r'""', 6), (r'"abc"', 9), (r'"aaa\"aaa"', 16), (r'"\x27"', 11)],
)
def test_size_encoded(line, expected):
    assert expected == size_encoded(line)
