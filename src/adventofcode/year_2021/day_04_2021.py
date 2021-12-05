from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def parse_boards(input_str: List[str]):
    curBoard: List[List[int]] = []
    for line in input_str:
        if len(line) == 0:
            yield curBoard
            curBoard = []
        else:
            curBoard.append([int(x) for x in line.split()])
    if curBoard:
        yield curBoard


def isWinner(board: List[List[int]], nums: List[int]):
    for i in range(5):
        rowWinner = True
        colWinner = True
        for j in range(5):
            if board[i][j] not in nums:
                rowWinner = False
                if not colWinner:
                    break
            if board[j][i] not in nums:
                colWinner = False
                if not rowWinner:
                    break
        if rowWinner or colWinner:
            return True
    return False


@solution_timer(2021, 4, 1)
def part_one(input_data: List[str]):
    nums = [int(x) for x in input_data[0].split(",")]
    input_data = input_data[2:]
    boards = list(parse_boards(input_data))

    for i in range(len(nums)):
        for board in boards:
            if isWinner(board, nums[: i + 1]):
                boardSum = 0
                for row in board:
                    for num in row:
                        if num not in nums[: i + 1]:
                            boardSum += num
                return boardSum * nums[i]
    raise SolutionNotFoundException(2021, 4, 1)


@solution_timer(2021, 4, 2)
def part_two(input_data: List[str]):
    nums = [int(x) for x in input_data[0].split(",")]
    input_data = input_data[2:]
    boards = list(parse_boards(input_data))

    for i in range(len(nums)):
        for board in boards:
            if isWinner(board, nums[: i + 1]):
                if len(boards) == 1:
                    boardSum = 0
                    for row in board:
                        for num in row:
                            if num not in nums[: i + 1]:
                                boardSum += num
                    return boardSum * nums[i]
                boards.remove(board)
    raise SolutionNotFoundException(2021, 4, 2)


if __name__ == "__main__":
    data = get_input_for_day(2021, 4)
    part_one(data)
    part_two(data)
