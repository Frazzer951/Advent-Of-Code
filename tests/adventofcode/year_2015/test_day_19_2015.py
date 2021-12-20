import pytest
from adventofcode.year_2015.day_19_2015 import numReplacements


@pytest.mark.parametrize(
    ["replacements", "molecule", "expected"],
    [({"H": ["HO", "OH"], "O": ["HH"]}, "HOH", 4), ({"H": ["HO", "OH"], "O": ["HH"]}, "HOHOHO", 7)],
)
def test_part_one(replacements, molecule, expected):
    assert expected == numReplacements(replacements, molecule)
