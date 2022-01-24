import pytest
from adventofcode.year_2021.day_12_2021 import part_one
from adventofcode.year_2021.day_12_2021 import part_two


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        (
            [
                "start-A",
                "start-b",
                "A-c",
                "A-b",
                "b-d",
                "A-end",
                "b-end",
            ],
            10,
        ),
        (
            [
                "dc-end",
                "HN-start",
                "start-kj",
                "dc-start",
                "dc-HN",
                "LN-dc",
                "HN-end",
                "kj-sa",
                "kj-HN",
                "kj-dc",
            ],
            19,
        ),
        (
            [
                "fs-end",
                "he-DX",
                "fs-he",
                "start-DX",
                "pj-DX",
                "end-zg",
                "zg-sl",
                "zg-pj",
                "pj-he",
                "RW-he",
                "fs-DX",
                "pj-RW",
                "zg-RW",
                "start-pj",
                "he-WI",
                "zg-he",
                "pj-fs",
                "start-RW",
            ],
            226,
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
                "start-A",
                "start-b",
                "A-c",
                "A-b",
                "b-d",
                "A-end",
                "b-end",
            ],
            36,
        ),
        (
            [
                "dc-end",
                "HN-start",
                "start-kj",
                "dc-start",
                "dc-HN",
                "LN-dc",
                "HN-end",
                "kj-sa",
                "kj-HN",
                "kj-dc",
            ],
            103,
        ),
        (
            [
                "fs-end",
                "he-DX",
                "fs-he",
                "start-DX",
                "pj-DX",
                "end-zg",
                "zg-sl",
                "zg-pj",
                "pj-he",
                "RW-he",
                "fs-DX",
                "pj-RW",
                "zg-RW",
                "start-pj",
                "he-WI",
                "zg-he",
                "pj-fs",
                "start-RW",
            ],
            3509,
        ),
    ],
)
def test_part_two(line, expected):
    assert expected == part_two(line)
