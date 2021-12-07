from adventofcode.year_2015.day_24_2015 import splitPresents


def test_part_one():
    t1 = splitPresents([1, 2, 3, 4, 5, 7, 8, 9, 10, 11], 3)
    assert t1 == 99


def test_part_two():
    t3 = splitPresents([1, 2, 3, 4, 5, 7, 8, 9, 10, 11], 4)
    assert t3 == 44
