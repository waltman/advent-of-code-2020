#!/usr/bin/env python3
from sys import argv
from itertools import combinations

filename = argv[1]
with open(filename) as f:
    data = [int(line) for line in f]

PREAMBLE = 25
for i in range(PREAMBLE, len(data)):
    if data[i] not in [sum(comb) for comb in combinations(data[i-PREAMBLE:i], 2)]:
        print('Part 1:', data[i])
        break

