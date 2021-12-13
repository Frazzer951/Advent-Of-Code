from typing import List, Dict, Set

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def pathfinder_1(nodes: Dict[str, Set[str]], node: str, history: List[str]):
    results = []
    new_history = history + [node]
    if node == "end":
        return [new_history]
    for neighbor in nodes[node]:
        if neighbor != "start" and (neighbor not in history or neighbor[0].isupper()):
            new_results = pathfinder_1(nodes, neighbor, new_history)
            results.extend(new_results)
    return results


def pathfinder_2(nodes: Dict[str, Set[str]], node: str, history: List[str]):
    results = []
    new_history = history + [node]
    if node == "end":
        return [new_history]
    for neighbor in nodes[node]:
        if neighbor != "start":
            if neighbor[0].isupper():
                new_results = pathfinder_2(nodes, neighbor, new_history)
                results.extend(new_results)
            else:
                smalls = [i for i in new_history if i[0].islower()]
                has_two = False
                for i in smalls:
                    if smalls.count(i) > 1:
                        has_two = True
                        break
                if (has_two and new_history.count(neighbor) < 1) or (not has_two and new_history.count(neighbor) < 2):
                    new_results = pathfinder_2(nodes, neighbor, new_history)
                    results.extend(new_results)
    return results


@solution_timer(2021, 12, 1)
def part_one(input_data: List[str]):
    nodes: Dict[str, Set[str]] = {}
    for line in input_data:
        n1, n2 = line.strip().split("-")
        if n1 in nodes:
            nodes[n1].add(n2)
        else:
            nodes[n1] = {n2}
        if n2 in nodes.keys():
            nodes[n2].add(n1)
        else:
            nodes[n2] = {n1}
    paths = pathfinder_1(nodes, "start", list())
    return len(paths)


@solution_timer(2021, 12, 2)
def part_two(input_data: List[str]):
    nodes: Dict[str, Set[str]] = {}
    for line in input_data:
        n1, n2 = line.strip().split("-")
        if n1 in nodes:
            nodes[n1].add(n2)
        else:
            nodes[n1] = {n2}
        if n2 in nodes.keys():
            nodes[n2].add(n1)
        else:
            nodes[n2] = {n1}
    paths = pathfinder_2(nodes, "start", list())
    return len(paths)


if __name__ == "__main__":
    data = get_input_for_day(2021, 12)
    part_one(data)
    part_two(data)
