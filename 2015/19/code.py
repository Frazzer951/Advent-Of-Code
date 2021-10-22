# Advent of code Year 2015 Day 19 solution
# Author = Frazzer951
# Date = October 2021

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")

molecule = input[-1].strip()
input = input[:-2]
replacements = dict()
for line in input:
    line = line.split(" => ")
    if line[0] not in replacements:
        replacements[line[0]] = [line[1]]
    else:
        replacements[line[0]].append(line[1])


def replace(molecule, start, end, replacement):
    return molecule[:start] + replacement + molecule[end:]


def numReplacements(replacements, molecule):
    newMolecules = []
    maxKeySize = max([len(key) for key in replacements])
    for i in range(len(molecule)):
        for j in range(maxKeySize):
            if molecule[i : i + j + 1] in replacements:
                for newMolecule in replacements[molecule[i : i + j + 1]]:
                    newMolecules.append(replace(molecule, i, i + j + 1, newMolecule))
    return len(set(newMolecules))


t1 = numReplacements({"H": ["HO", "OH"], "O": ["HH"]}, "HOH")
assert t1 == 4, f"t1, {t1}, is not 4 in Part One Test 1"
print("Part One Test 1: " + str(t1))

t2 = numReplacements({"H": ["HO", "OH"], "O": ["HH"]}, "HOHOHO")
assert t2 == 7, f"t2, {t2}, is not 7 is Part One Test 2"
print("Part One Test 2: " + str(t2))


p1 = numReplacements(replacements, molecule)
print("Part One : " + str(p1))

# print(molecule)
molecule = molecule.replace("Rn", "(")
molecule = molecule.replace("Ar", ")")
molecule = molecule.replace("Y", ",")
# print(molecule)
for key in replacements:
    molecule = molecule.replace(key, "X")
# print(molecule)
count = len(molecule)
Rn = molecule.count("(")
Ar = molecule.count(")")
RnAr = Rn + Ar
Y = molecule.count(",")
p2 = count - RnAr - 2 * Y - 1
# print(f"Count: {count}, Rn: {Rn}, Ar: {Ar}, RnAr: {RnAr}, Y: {Y}")
# print(f"Count - RnAr - 2*Y - 1 = {p2}")
print("Part Two : " + str(p2))