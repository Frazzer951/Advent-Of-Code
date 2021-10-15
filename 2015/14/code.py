# Advent of code Year 2015 Day 14 solution
# Author = Frazzer951
# Date = October 2021

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


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


def part1(input, seconds):
    maxDistance = 0
    for line in input:
        split_line = line.split()
        speed = int(split_line[3])
        time = int(split_line[6])
        rest = int(split_line[13])
        dist = get_distance(speed, time, rest, seconds)
        maxDistance = max(maxDistance, dist)
    return maxDistance


t1 = part1(
    [
        "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
        "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
    ],
    1000,
)
print("Part One Test 1: " + str(t1))

p1 = part1(input, 2503)
print("Part One : " + str(p1))


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


def part2(input, seconds):
    distances = []
    for line in input:
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


t3 = part2(
    [
        "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
        "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
    ],
    1000,
)
print("Part Two Test 1: " + str(t3))

p2 = part2(input, 2503)
print("Part Two : " + str(p2))