from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def replace(molecule, start, end, replacement):
    return molecule[:start] + replacement + molecule[end:]


def numReplacements(replacements, molecule):
    newMolecules = []
    maxKeySize = max([len(key) for key in replacements])
    for i in range(len(molecule)):
        for j in range(maxKeySize):
            if molecule[i: i + j + 1] in replacements:
                for newMolecule in replacements[molecule[i: i + j + 1]]:
                    newMolecules.append(replace(molecule, i, i + j + 1, newMolecule))
    return len(set(newMolecules))


@solution_timer(2015, 19, 1)
def part_one(input_data: List[str]):
    molecule = input_data[-1].strip()
    input_data = input_data[:-2]
    replacements = dict()
    for line in input_data:
        replace = line.split(" => ")
        if replace[0] not in replacements:
            replacements[replace[0]] = [replace[1]]
        else:
            replacements[replace[0]].append(replace[1])
    return numReplacements(replacements, molecule)


@solution_timer(2015, 19, 2)
def part_two(input_data: List[str]):
    molecule = input_data[-1].strip()
    input_data = input_data[:-2]
    replacements = dict()
    for line in input_data:
        replace = line.split(" => ")
        if replace[0] not in replacements:
            replacements[replace[0]] = [replace[1]]
        else:
            replacements[replace[0]].append(replace[1])
    molecule = molecule.replace("Rn", "(")
    molecule = molecule.replace("Ar", ")")
    molecule = molecule.replace("Y", ",")
    for key in replacements:
        molecule = molecule.replace(key, "X")
    count = len(molecule)
    Rn = molecule.count("(")
    Ar = molecule.count(")")
    RnAr = Rn + Ar
    Y = molecule.count(",")
    return count - RnAr - 2 * Y - 1


if __name__ == "__main__":
    data = get_input_for_day(2015, 19)
    part_one(data)
    part_two(data)
