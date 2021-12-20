import pytest
from adventofcode.year_2016.day_09_2016 import part_one, part_two


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("ADVENT", 6),
        ("A(1x5)BC", 7),
        ("(3x3)XYZ", 9),
        ("A(2x2)BCD(2x2)EFG", 11),
        ("(6x1)(1x3)A", 6),
        ("X(8x2)(3x3)ABCY", 18),
    ],
)
def test_part_one(line, expected):
    assert expected == part_one([line])


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("(3x3)XYZ", 9),
        ("X(8x2)(3x3)ABCY", 20),
        ("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920),
        ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445),
    ],
)
def test_part_two(line, expected):
    assert expected == part_two([line])
