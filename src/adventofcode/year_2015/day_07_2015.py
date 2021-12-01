from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


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


@solution_timer(2015, 7, 1)
def part_one(input_data: List[str], all_signals: bool = False):
    wires = [Wire(line) for line in input_data]

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
    if all_signals:
        return signals
    return signals["a"]


@solution_timer(2015, 7, 2)
def part_two(input_data: List[str], all_signals: bool = False):
    wires = [Wire(line) for line in input_data]
    wires = [wire for wire in wires if wire.output != "b"]

    signals = {"b": 3176}
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
    if all_signals:
        return signals
    return signals["a"]


if __name__ == "__main__":
    data = get_input_for_day(2015, 7)
    part_one(data)
    part_two(data)
