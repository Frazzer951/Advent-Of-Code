import pytest
from adventofcode.year_2021.day_16_2021 import part_one
from adventofcode.year_2021.day_16_2021 import part_two


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ],
)
def test_part_one(line, expected):
    assert expected == part_one([line])


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("C200B40A82", 3),
        ("04005AC33890", 54),
        ("880086C3E88112", 7),
        ("CE00C43D881120", 9),
        ("D8005AC2A8F0", 1),
        ("F600BC2D8F", 0),
        ("9C005AC2F8F0", 0),
        ("9C0141080250320F1802104A08", 1),
    ],
)
def test_part_two(line, expected):
    assert expected == part_two([line])
