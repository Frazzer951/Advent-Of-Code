from adventofcode.year_2016.day_02_2016 import decipherCode


def test_decipherCode_part_one():
    assert '1985' == decipherCode(["ULL", "RRDDD", "LURDL", "UUUUD"])


def test_decipherCode_part_two():
    keypad = [
        [None, None, 1, None, None],
        [None, 2, 3, 4, None],
        [5, 6, 7, 8, 9],
        [None, "A", "B", "C", None],
        [None, None, "D", None, None],
    ]
    assert "5DB3" == decipherCode(["ULL", "RRDDD", "LURDL", "UUUUD"], keypad, 0, 2)
