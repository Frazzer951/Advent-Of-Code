from adventofcode.year_2015.day_23_2015 import sim_code


def test_part_one():
    t1 = sim_code(
        [
            "inc a",
            "jio a, +2",
            "tpl a",
            "inc a  ",
        ]
    )
    assert t1["a"] == 2
