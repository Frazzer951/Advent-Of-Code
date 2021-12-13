import pytest
from adventofcode.year_2021.day_11_2021 import part_one, part_two, next_step


@pytest.mark.parametrize(
    ["input", "expected", "count"],
    [
        (
            [
                "11111",
                "19991",
                "19191",
                "19991",
                "11111",
            ],
            [
                "34543",
                "40004",
                "50005",
                "40004",
                "34543",
            ],
            9,
        ),
        (
            [
                "34543",
                "40004",
                "50005",
                "40004",
                "34543",
            ],
            [
                "45654",
                "51115",
                "61116",
                "51115",
                "45654",
            ],
            0,
        ),
        (
            [
                "5483143223",
                "2745854711",
                "5264556173",
                "6141336146",
                "6357385478",
                "4167524645",
                "2176841721",
                "6882881134",
                "4846848554",
                "5283751526",
            ],
            [
                "6594254334",
                "3856965822",
                "6375667284",
                "7252447257",
                "7468496589",
                "5278635756",
                "3287952832",
                "7993992245",
                "5957959665",
                "6394862637",
            ],
            0,
        ),
        (
            [
                "6594254334",
                "3856965822",
                "6375667284",
                "7252447257",
                "7468496589",
                "5278635756",
                "3287952832",
                "7993992245",
                "5957959665",
                "6394862637",
            ],
            [
                "8807476555",
                "5089087054",
                "8597889608",
                "8485769600",
                "8700908800",
                "6600088989",
                "6800005943",
                "0000007456",
                "9000000876",
                "8700006848",
            ],
            35,
        ),
    ],
)
def test_next_step(input, expected, count):
    input = [[int(x) for x in line] for line in input]
    expected = [[int(x) for x in line] for line in expected]
    result = next_step(input)
    assert expected == result[0]
    assert count == result[1]


def test_part_one():
    assert 1656 == part_one(
        [
            "5483143223",
            "2745854711",
            "5264556173",
            "6141336146",
            "6357385478",
            "4167524645",
            "2176841721",
            "6882881134",
            "4846848554",
            "5283751526",
        ]
    )


def test_part_two():
    assert 195 == part_two(
        [
            "5483143223",
            "2745854711",
            "5264556173",
            "6141336146",
            "6357385478",
            "4167524645",
            "2176841721",
            "6882881134",
            "4846848554",
            "5283751526",
        ]
    )