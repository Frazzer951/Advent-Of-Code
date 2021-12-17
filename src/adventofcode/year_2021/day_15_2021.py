from typing import List, Dict, Tuple

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

import math
import heapq
from collections import defaultdict


class Node:
    def __init__(self, weight, pos):
        self.weight = weight
        self.pos = pos
        self.neighbors = set()

    def __repr__(self):
        return f"({self.pos[0]},{self.pos[1]}): {self.weight}"

    def __str__(self):
        return f"({self.pos[0]},{self.pos[1]}): {self.weight}"

    def __lt__(self, other):
        return self.weight < other.weight

    def add_neighbor(self, node):
        self.neighbors.add(node)


def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]


def distance(node, end):
    return math.sqrt((node.pos[0] - end.pos[0]) ** 2 + (node.pos[1] - end.pos[1]) ** 2)


def a_star(start, end):
    openSet: List[Tuple[int, Node]] = [(0, start)]
    cameFrom: Dict[Node, Node] = {}
    gScore: Dict[Node, float] = defaultdict(lambda: math.inf)
    gScore[start] = 0
    fScore = defaultdict(lambda: math.inf)
    fScore[start] = distance(start, end)

    while len(openSet) > 0:
        current = heapq.heappop(openSet)
        curr_node = current[1]
        if curr_node == end:
            return reconstruct_path(cameFrom, curr_node)
        for neighbor in curr_node.neighbors:
            tentative_gScore = gScore[curr_node] + neighbor.weight
            if tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = curr_node
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + distance(neighbor, end)
                heapq.heappush(openSet, (fScore[neighbor], neighbor))
    return []


@solution_timer(2021, 15, 1)
def part_one(input_data: List[str]):
    data = [[int(x) for x in row] for row in input_data]
    width = len(data[0])
    height = len(data)
    nodes = [Node(data[row][col], (row, col)) for row in range(height) for col in range(width)]
    for row in range(len(data)):
        for col in range(len(data[row])):
            curr_idx = row * width + col
            dirs = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            for dir in dirs:
                if dir[0] >= 0 and dir[0] < height and dir[1] >= 0 and dir[1] < width:
                    row_idx = dir[0] * width + dir[1]
                    # print(f'curr_idx: {curr_idx}, row_idx: {row_idx}')
                    nodes[curr_idx].add_neighbor(nodes[row_idx])
                    nodes[row_idx].add_neighbor(nodes[curr_idx])
    path = a_star(nodes[0], nodes[-1])
    # print(path)
    path = path[1:]
    path_weight = sum([node.weight for node in path])
    return path_weight


def part_2_input_mod(og_data):
    width = len(og_data[0])
    height = len(og_data)
    data = [[0 for _ in range(len(og_data[0] * 5))] for _ in range(len(og_data) * 5)]
    for row in range(len(og_data)):
        for col in range(len(og_data[row])):
            for i in range(5):
                for j in range(5):
                    data[row + (height * i)][col + (width * j)] = og_data[row][col] + i + j
                    while data[row + (height * i)][col + (width * j)] > 9:
                        data[row + (height * i)][col + (width * j)] -= 9
    return data


@solution_timer(2021, 15, 2)
def part_two(input_data: List[str]):
    og_data = [[int(x) for x in row] for row in input_data]
    data = part_2_input_mod(og_data)
    width = len(data[0])
    height = len(data)
    nodes = [Node(data[row][col], (row, col)) for row in range(height) for col in range(width)]
    for row in range(len(data)):
        for col in range(len(data[row])):
            curr_idx = row * width + col
            dirs = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            for dir in dirs:
                if dir[0] >= 0 and dir[0] < height and dir[1] >= 0 and dir[1] < width:
                    row_idx = dir[0] * width + dir[1]
                    # print(f'curr_idx: {curr_idx}, row_idx: {row_idx}')
                    nodes[curr_idx].add_neighbor(nodes[row_idx])
                    nodes[row_idx].add_neighbor(nodes[curr_idx])
    path = a_star(nodes[0], nodes[-1])
    # print(path)
    path = path[1:]
    path_weight = sum([node.weight for node in path])
    return path_weight


if __name__ == "__main__":
    data = get_input_for_day(2021, 15)
    part_one(data)
    part_two(data)
