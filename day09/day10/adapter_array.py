#!/usr/bin/env python3
from sys import argv
from functools import cache

adapter_set = set()

@cache
def paths_to(a, b):
    if a == b:
        return 1
    else:
        tot = 0
        for i in range(1,4):
            if i in adapter_set:
                tot += paths_to(i, b)
        return tot

filename = argv[1]
with open(filename) as f:
    adapters = [int(line) for line in f]

adapters += [0, max(adapters) + 3]
adapters.sort()

diff1, diff3 = 0,0
for i in range(1, len(adapters)):
    if (diff := adapters[i] - adapters[i-1]) == 1:
        diff1 += 1
    elif diff == 3:
        diff3 += 1

print(diff1, diff3, diff1 * diff3)
print('Part 1:', diff1 * diff3)

adapter_set = set(adapters)
print('Part 2:', paths_to(0, adapters[-1]))
