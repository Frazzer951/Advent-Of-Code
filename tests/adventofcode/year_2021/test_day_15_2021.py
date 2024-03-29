from adventofcode.year_2021.day_15_2021 import part_2_input_mod
from adventofcode.year_2021.day_15_2021 import part_one
from adventofcode.year_2021.day_15_2021 import part_two


def test_part_one():
    assert 40 == part_one(
        [
            "1163751742",
            "1381373672",
            "2136511328",
            "3694931569",
            "7463417111",
            "1319128137",
            "1359912421",
            "3125421639",
            "1293138521",
            "2311944581",
        ]
    )


def test_part_2_input_mod():
    assert [
        [8, 9, 1, 2, 3],
        [9, 1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6],
        [3, 4, 5, 6, 7],
    ] == part_2_input_mod([[8]])


def test_part_two():
    assert 315 == part_two(
        [
            "1163751742",
            "1381373672",
            "2136511328",
            "3694931569",
            "7463417111",
            "1319128137",
            "1359912421",
            "3125421639",
            "1293138521",
            "2311944581",
        ]
    )
