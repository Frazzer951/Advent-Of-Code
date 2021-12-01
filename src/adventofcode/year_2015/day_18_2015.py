from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def countNeighbors(board, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x + i < 0 or x + i >= len(board) or y + j < 0 or y + j >= len(board[0]):
                continue
            if i == 0 and j == 0:
                continue
            if board[x + i][y + j] == "#":
                count += 1
    return count


def nextStep(board):
    newBoard = [["." for i in range(len(board[0]))] for j in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            neighbors = countNeighbors(board, i, j)
            if board[i][j] == "#" and (neighbors == 2 or neighbors == 3):
                newBoard[i][j] = "#"
            if board[i][j] == "." and neighbors == 3:
                newBoard[i][j] = "#"
    return newBoard


def iterateBoard(board, iterations):
    for i in range(iterations):
        board = nextStep(board)
    return board


def nextStep2(board):
    newBoard = [["." for i in range(len(board[0]))] for j in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            neighbors = countNeighbors(board, i, j)
            if board[i][j] == "#" and (neighbors == 2 or neighbors == 3):
                newBoard[i][j] = "#"
            if board[i][j] == "." and neighbors == 3:
                newBoard[i][j] = "#"
    newBoard[0][0] = "#"
    newBoard[0][-1] = "#"
    newBoard[-1][0] = "#"
    newBoard[-1][-1] = "#"
    return newBoard


def iterateBoard2(board, iterations):
    board[0][0] = "#"
    board[0][-1] = "#"
    board[-1][0] = "#"
    board[-1][-1] = "#"
    for i in range(iterations):
        board = nextStep2(board)
    return board


@solution_timer(2015, 18, 1)
def part_one(input_data: List[str]):
    input_data = [list(line) for line in input_data]
    p1 = iterateBoard(input_data, 100)
    return sum([lst.count("#") for lst in p1])


@solution_timer(2015, 18, 2)
def part_two(input_data: List[str]):
    input_data = [list(line) for line in input_data]
    p2 = iterateBoard2(input_data, 100)
    return sum([lst.count("#") for lst in p2])


if __name__ == "__main__":
    data = get_input_for_day(2015, 18)
    part_one(data)
    part_two(data)
