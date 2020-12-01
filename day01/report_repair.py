#!/usr/bin/env python3
from sys import argv
from itertools import combinations

filename = argv[1]
with open(filename) as f:
    entries = [int(line) for line in f]

for pair in combinations(entries, 2):
    if sum(pair) == 2020:
        res = pair[0] * pair[1]
        break
print('Part 1:', res)

for pair in combinations(entries, 3):
    if sum(pair) == 2020:
        res = pair[0] * pair[1] * pair[2]
        break
print('Part 2:', res)
