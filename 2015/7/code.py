# Advent of code Year 2015 Day 7 solution
# Author = Frazzer951
# Date = October 2021

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


class Wire:
    def __init__(self, line):
        self._line = line
        self.parseLine(line)

    def parseLine(self, line):
        sLine = line.split()
        self.output = sLine[-1]
        left = sLine[:-2]
        self.op = "ASSIGN"
        for op in ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"]:
            if op in left:
                self.op = op
                left.remove(op)
        self.inputs = [int(i) if i.isdigit() else i for i in left]

    def evaluate(self):
        if self.op == "ASSIGN":
            return int(self.inputs[0])
        elif self.op == "AND":
            return int(self.inputs[0] & self.inputs[1])
        elif self.op == "OR":
            return int(self.inputs[0] | self.inputs[1])
        elif self.op == "NOT":
            return int(65535 - self.inputs[0])
        elif self.op == "LSHIFT":
            return int(self.inputs[0] << self.inputs[1])
        elif self.op == "RSHIFT":
            return int(self.inputs[0] >> self.inputs[1])
        else:
            raise ValueError("invalid operator")

    def fillInputs(self, signals):
        self.inputs = [signals[i] if i in signals else i for i in self.inputs]

    def isComplete(self):
        return all([isinstance(i, int) for i in self.inputs])


def part1(input):
    wires = [Wire(line) for line in input]

    signals = {}
    localWires = list(wires)
    while len(localWires) != 0:
        newWires = []
        for wire in localWires:
            if wire.isComplete():
                signals[wire.output] = wire.evaluate()
            else:
                wire.fillInputs(signals)
                newWires.append(wire)
        localWires = newWires
    return signals


t1 = part1(
    [
        "123 -> x",
        "456 -> y",
        "x AND y -> d",
        "x OR y -> e",
        "x LSHIFT 2 -> f",
        "y RSHIFT 2 -> g",
        "NOT x -> h",
        "NOT y -> i",
    ]
)
print("Part One Test 1: " + str(t1))

p1 = part1(input)
print("Part One : a = " + str(p1["a"]))


def part2(input, signals={}):
    wires = [Wire(line) for line in input]
    wires = [wire for wire in wires if wire.output != "b"]

    localWires = list(wires)
    while len(localWires) != 0:
        newWires = []
        for wire in localWires:
            if wire.isComplete():
                signals[wire.output] = wire.evaluate()
            else:
                wire.fillInputs(signals)
                newWires.append(wire)
        localWires = newWires
    return signals


p2 = part2(input, {"b": p1["a"]})
print("Part Two : a = " + str(p2["a"]))
