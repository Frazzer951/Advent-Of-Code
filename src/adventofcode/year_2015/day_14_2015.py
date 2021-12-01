from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def get_distance(speed, time, rest, seconds):
    distance = 0
    fly = True
    while seconds:
        if fly:
            flySeconds = min(seconds, time)
            distance += speed * flySeconds
            seconds -= flySeconds
            fly = False
        else:
            restSeconds = min(seconds, rest)
            seconds -= restSeconds
            fly = True
    return distance


def get_distances(speed, time, rest, seconds):
    fly = True
    distance = 0
    flyTime = time
    restTime = rest
    distances = [0] * seconds

    for i in range(seconds):
        if fly:
            distance += speed
            flyTime -= 1
            if flyTime == 0:
                fly = False
                flyTime = time
        else:
            restTime -= 1
            if restTime == 0:
                fly = True
                restTime = rest
        distances[i] = distance
    return distances


@solution_timer(2015, 14, 1)
def part_one(input_data: List[str], seconds: int = 2503):
    maxDistance = 0
    for line in input_data:
        split_line = line.split()
        speed = int(split_line[3])
        time = int(split_line[6])
        rest = int(split_line[13])
        dist = get_distance(speed, time, rest, seconds)
        maxDistance = max(maxDistance, dist)
    return maxDistance


@solution_timer(2015, 14, 2)
def part_two(input_data: List[str], seconds: int = 2503):
    distances = []
    for line in input_data:
        split_line = line.split()
        speed = int(split_line[3])
        time = int(split_line[6])
        rest = int(split_line[13])
        dist = get_distances(speed, time, rest, seconds)
        distances.append(dist)

    scores = [0] * len(distances)

    for i in range(seconds):
        maxDist = [0, []]
        for j in range(len(distances)):
            if distances[j][i] > maxDist[0]:
                maxDist[0] = distances[j][i]
                maxDist[1] = [j]
            elif distances[j][i] == maxDist[0]:
                maxDist[1].append(j)
        addPoints = set(maxDist[1])
        for num in addPoints:
            scores[num] += 1

    return max(scores)


if __name__ == "__main__":
    data = get_input_for_day(2015, 14)
    part_one(data)
    part_two(data)
