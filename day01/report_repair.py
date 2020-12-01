#!/usr/bin/env python3
from sys import argv
from itertools import combinations
from operator import mul
from functools import reduce

def find_result(entries, k):
    for comb in combinations(entries, k):
        if sum(comb) == 2020:
            return reduce(mul, comb, 1)

filename = argv[1]
with open(filename) as f:
    entries = [int(line) for line in f]

print('Part 1:', find_result(entries, 2))
print('Part 2:', find_result(entries, 3))
