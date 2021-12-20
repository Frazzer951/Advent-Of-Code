import pytest
from adventofcode.year_2016.day_04_2016 import is_real, decrypt_name, part_one


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("aaaaa-bbb-z-y-x-123[abxyz]", True),
        ("a-b-c-d-e-f-g-h-987[abcde]", True),
        ("not-a-real-room-404[oarel]", True),
        ("totally-real-room-200[decoy]", False),
    ],
)
def test_is_real(line, expected):
    assert expected == is_real(line)


def test_part_one():
    assert 1514 == part_one(
        [
            "aaaaa-bbb-z-y-x-123[abxyz]",
            "a-b-c-d-e-f-g-h-987[abcde]",
            "not-a-real-room-404[oarel]",
            "totally-real-room-200[decoy]",
        ]
    )


def test_decrypt_name():
    assert "very encrypted name" == decrypt_name("qzmt-zixmtkozy-ivhz-343[zimth]")
