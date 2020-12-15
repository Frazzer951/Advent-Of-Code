# Advent of code Year 2020 Day 13 solution
# Author = Frazzer951
# Date = December 2020

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().split('\n')

def get_buses(schedules):
    buses = []
    for bus in schedules.split(','):
        if bus == 'x': continue
        buses.append(int(bus))
    return buses

def check_time(buses, time):
    for bus in buses:
        if time % bus == 0:
            return bus
    return -1

def soonest_bus(data):
    cur_time = int(data[0])
    buses = get_buses(data[1])
    time = cur_time
    while True:
        bus = check_time(buses, time)
        if bus != -1: break
        time += 1
    return (time - cur_time) * bus
        

test_input = """939
7,13,x,x,59,x,31,19""".split('\n')


print("Test Input : "+ str(soonest_bus(test_input)))



print("Part One : "+ str(soonest_bus(input)))



print("Part Two : "+ str(None))