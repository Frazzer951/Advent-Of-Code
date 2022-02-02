import pytest
from adventofcode.year_2020.day_10_2020 import part_one
from adventofcode.year_2020.day_10_2020 import part_two


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        (
            [
                "16",
                "10",
                "15",
                "5",
                "1",
                "11",
                "7",
                "19",
                "6",
                "12",
                "4",
            ],
            35,
        ),
        (
            [
                "28",
                "33",
                "18",
                "42",
                "31",
                "14",
                "46",
                "20",
                "48",
                "47",
                "24",
                "23",
                "49",
                "45",
                "19",
                "38",
                "39",
                "11",
                "1",
                "32",
                "25",
                "35",
                "8",
                "17",
                "7",
                "9",
                "4",
                "2",
                "34",
                "10",
                "3",
            ],
            220,
        ),
    ],
)
def test_part_one(line, expected):
    assert expected == part_one(line)


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        (
            [
                "16",
                "10",
                "15",
                "5",
                "1",
                "11",
                "7",
                "19",
                "6",
                "12",
                "4",
            ],
            8,
        ),
        (
            [
                "28",
                "33",
                "18",
                "42",
                "31",
                "14",
                "46",
                "20",
                "48",
                "47",
                "24",
                "23",
                "49",
                "45",
                "19",
                "38",
                "39",
                "11",
                "1",
                "32",
                "25",
                "35",
                "8",
                "17",
                "7",
                "9",
                "4",
                "2",
                "34",
                "10",
                "3",
            ],
            19208,
        ),
    ],
)
def test_part_two(line, expected):
    assert expected == part_two(line)
