from adventofcode.year_2017.day_02_2017 import part_one
from adventofcode.year_2017.day_02_2017 import part_two


def test_part_one():
    assert 18 == part_one(
        [
            "5\t1\t9\t5",
            "7\t5\t3",
            "2\t4\t6\t8",
        ]
    )


def test_part_two():
    assert 9 == part_two(
        [
            "5\t9\t2\t8",
            "9\t4\t7\t3",
            "3\t8\t6\t5",
        ]
    )
