# Advent of code Year 2015 Day 18 solution
# Author = Frazzer951
# Date = October 2021

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")
input = [list(line) for line in input]


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


t1 = iterateBoard(
    [
        [".", "#", ".", "#", ".", "#"],
        [".", ".", ".", "#", "#", "."],
        ["#", ".", ".", ".", ".", "#"],
        [".", ".", "#", ".", ".", "."],
        ["#", ".", "#", ".", ".", "#"],
        ["#", "#", "#", "#", ".", "."],
    ],
    4,
)
count = sum([lst.count("#") for lst in t1])
assert t1 == [
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", "#", "#", ".", "."],
    [".", ".", "#", "#", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
]
assert count == 4
print("Part One Test 1: " + str(count))

p1 = iterateBoard(input, 100)
count = sum([lst.count("#") for lst in p1])
print("Part One : " + str(count))


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


t3 = iterateBoard2(
    [
        ["#", "#", ".", "#", ".", "#"],
        [".", ".", ".", "#", "#", "."],
        ["#", ".", ".", ".", ".", "#"],
        [".", ".", "#", ".", ".", "."],
        ["#", ".", "#", ".", ".", "#"],
        ["#", "#", "#", "#", ".", "#"],
    ],
    5,
)
count = sum([lst.count("#") for lst in t3])
assert t3 == [
    ["#", "#", ".", "#", "#", "#"],
    [".", "#", "#", ".", ".", "#"],
    [".", "#", "#", ".", ".", "."],
    [".", "#", "#", ".", ".", "."],
    ["#", ".", "#", ".", ".", "."],
    ["#", "#", ".", ".", ".", "#"],
]
assert count == 17
print("Part Two Test 1: " + str(count))

p2 = iterateBoard2(input, 100)
count = sum([lst.count("#") for lst in p2])
print("Part Two : " + str(count))