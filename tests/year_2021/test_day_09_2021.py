from adventofcode.year_2021.day_09_2021 import part_one, part_two


def test_part_one():
    assert 15 == part_one(
        [
            "2199943210",
            "3987894921",
            "9856789892",
            "8767896789",
            "9899965678",
        ]
    )


def test_part_two():
    assert 1134 == part_two(
        [
            "2199943210",
            "3987894921",
            "9856789892",
            "8767896789",
            "9899965678",
        ]
    )
