from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2021, 9, 1)
def part_one(input_data: List[str]):
    input_data = [[int(x) for x in row] for row in input_data]

    risk_level = 0

    for j in range(len(input_data)):
        for i in range(len(input_data[j])):
            if j - 1 >= 0:
                if input_data[j - 1][i] <= input_data[j][i]:
                    continue
            if j + 1 < len(input_data):
                if input_data[j + 1][i] <= input_data[j][i]:
                    continue
            if i - 1 >= 0:
                if input_data[j][i - 1] <= input_data[j][i]:
                    continue
            if i + 1 < len(input_data[j]):
                if input_data[j][i + 1] <= input_data[j][i]:
                    continue
            risk_level += input_data[j][i] + 1
            # print(f"{input_data[j][i]}: {j} {i}")
    return risk_level


def fillBasin(row, col, heatMap, basin):
    target = heatMap[row][col]
    if target == 9:
        return
    heatMap[row][col] = 9
    basin.append(target)
    if row > 0:
        fillBasin(row - 1, col, heatMap, basin)
    if row < len(heatMap) - 1:
        fillBasin(row + 1, col, heatMap, basin)
    if col > 0:
        fillBasin(row, col - 1, heatMap, basin)
    if col < len(heatMap[row]) - 1:
        fillBasin(row, col + 1, heatMap, basin)
    return


@solution_timer(2021, 9, 2)
def part_two(input_data: List[str]):
    heatMap = [[int(x) for x in row] for row in input_data]
    basins: List[List[int]] = []
    basin: List[int] = []
    for row in range(len(heatMap)):
        for col in range(len(heatMap[row])):
            fillBasin(row, col, heatMap, basin)
            if basin:
                basins.append(basin)
                basin = []
    basinSizes = [len(basin) for basin in basins]
    basinSizes.sort()
    largestBasins = basinSizes[-3:]
    finalProduct = 1
    for basin in largestBasins:
        finalProduct *= basin
    return finalProduct


if __name__ == "__main__":
    data = get_input_for_day(2021, 9)
    part_one(data)
    part_two(data)
