#!/usr/bin/env python3
from sys import argv

best_id = -1
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        row = int(line[:7].translate(str.maketrans('FB','01')), 2)
        col = int(line[7:].translate(str.maketrans('LR','01')), 2)
        seat_id = row * 8 + col
        best_id = max(best_id, seat_id)
#        print(line, row, col, seat_id)

print('Part 1:', best_id)
