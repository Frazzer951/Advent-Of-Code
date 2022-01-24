from adventofcode.year_2015.day_17_2015 import find_combinations
from adventofcode.year_2015.day_17_2015 import find_different_ways


def test_part_one():
    assert 4 == find_combinations(["20", "15", "10", "5", "5"], 25)


def test_part_two():
    assert 3 == find_different_ways(["20", "15", "10", "5", "5"], 25)
