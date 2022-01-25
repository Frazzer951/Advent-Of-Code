from adventofcode.year_2020.day_08_2020 import part_one
from adventofcode.year_2020.day_08_2020 import part_two


def test_part_one():
    assert 5 == part_one(
        [
            "nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6",
        ]
    )


def test_part_two():
    assert 8 == part_two(
        [
            "nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6",
        ]
    )
