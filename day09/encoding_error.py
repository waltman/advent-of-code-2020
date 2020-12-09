#!/usr/bin/env python3
from sys import argv
from itertools import combinations

filename = argv[1]
with open(filename) as f:
    data = [int(line) for line in f]

PREAMBLE = 25
for i in range(PREAMBLE, len(data)):
    if data[i] not in [sum(comb) for comb in combinations(data[i-PREAMBLE:i], 2)]:
        invalid_number = data[i]
        break
print('Part 1:', invalid_number)

# solve part 2
found = False
for i in range(len(data)):
    if found:
        break
    for j in range(i+1, len(data)+1):
        if (tot := sum(data[i:j]) == invalid_number):
            print('Part 2:', min(data[i:j]) + max(data[i:j]))
            found = True
            break
        elif tot > invalid_number:
            break
