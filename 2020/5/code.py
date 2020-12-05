# Advent of code Year 2020 Day 5 solution
# Author = Frazzer951
# Date = December 2020

import math

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

def binary_split(lower, upper, half): 
    split = math.floor((upper - lower)/2)
    if half == 'u':
        #print('Lower: {}, Upper: {}'.format(lower+split+1, upper))
        return lower+split+1, upper
    if half == 'l':
        #print('Lower: {}, Upper: {}'.format(lower, lower+split))
        return lower, lower+split

def find_seat(seat_str):
    row_str = seat_str[:7]
    col_str = seat_str[7:]
    #print('row_str: {}, col_str: {}'.format(row_str, col_str))

    max_seat_row = 127
    min_seat_row = 0
    for char in row_str:
        if char == 'F':
            min_seat_row, max_seat_row = binary_split(min_seat_row, max_seat_row, 'l')
        if char == 'B':
            min_seat_row, max_seat_row = binary_split(min_seat_row, max_seat_row, 'u')
    
    max_seat_col = 7
    min_seat_col = 0
    for char in col_str:
        if char == 'L':
            min_seat_col, max_seat_col = binary_split(min_seat_col, max_seat_col, 'l')
        if char == 'R':
            min_seat_col, max_seat_col = binary_split(min_seat_col, max_seat_col, 'u')

    return max_seat_row, max_seat_col

def get_seat_ids(seat_strings):
    highest_id = 0
    for seat_str in seat_strings:
        row, col = find_seat(seat_str)
        seat_id = row*8+col
        #print('{}: row: {}, col: {}, seat ID: {}.'.format(seat_str, row, col, seat_id))
        if seat_id > highest_id:
            highest_id = seat_id
    return highest_id

test_str = ['FBFBBFFRLR','BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL']
get_seat_ids(test_str)

print("Part One : "+ str(get_seat_ids(input)))

def find_empty_seat(seat_strings):
    seat_ids = []
    free_seat_ids = []

    for line in seat_strings:
        row, col = find_seat(line)
        seat_id = row*8+col
        seat_ids.append(seat_id)

    for row in range(0, 128):
        for col in range(0, 8):
            seat_id = row*8+col
            if seat_id not in seat_ids:
                #print('{} is not taken'.format(seat_id))
                free_seat_ids.append(seat_id)

    for ids in free_seat_ids:
        prev_id = ids-1
        next_id = ids+1
        if prev_id < 0: continue
        if prev_id in seat_ids and next_id in seat_ids:
            #print('{} is a valid seat'.format(ids))
            return ids


print("Part Two : "+ str(find_empty_seat(input)))