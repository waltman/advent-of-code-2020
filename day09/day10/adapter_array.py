#!/usr/bin/env python3
from sys import argv


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
