#!/usr/bin/env python3
from sys import argv

def calc_seat_id(row, col):
    return row * 8 + col

best_id = -1
min_row = 1e300
max_row = -1
seats = set()
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        row = int(line[:7].translate(str.maketrans('FB','01')), 2)
        col = int(line[7:].translate(str.maketrans('LR','01')), 2)
        seat_id = calc_seat_id(row, col)
        best_id = max(best_id, seat_id)
        min_row = min(min_row, row)
        max_row = max(max_row, row)
        seats.add((row, col))

print('Part 1:', best_id)

for row in range(min_row+1, max_row):
    for col in range(0,8):
        if (row,col) not in seats:
            print('Part 2:', calc_seat_id(row, col))
