import pytest
from adventofcode.year_2016.day_07_2016 import does_support_ssl
from adventofcode.year_2016.day_07_2016 import does_support_tls


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("abba[mnop]qrst", True),
        ("abcd[bddb]xyyx", False),
        ("aaaa[qwer]tyui", False),
        ("ioxxoj[asdfgh]zxcvbn", True),
    ],
)
def test_does_support_tls(line, expected):
    assert expected == does_support_tls(line)


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("aba[bab]xyz", True),
        ("xyx[xyx]xyx", False),
        ("aaa[kek]eke", True),
        ("zazbz[bzb]cdb", True),
    ],
)
def test_does_support_ssl(line, expected):
    assert expected == does_support_ssl(line)
