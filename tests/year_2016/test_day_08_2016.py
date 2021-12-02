from adventofcode.year_2016.day_08_2016 import part_one


def test_part_one():
    assert 6 == part_one(
        [
            "rect 3x2",
            "rotate column x=1 by 1",
            "rotate row y=0 by 4",
            "rotate column x=1 by 1",
        ],
        7,
        3,
    )
