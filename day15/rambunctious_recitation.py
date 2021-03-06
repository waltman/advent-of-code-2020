#!/usr/bin/env python3
from sys import argv

def do_turn(last_seen, t, last):
    prev = last_seen[last]
    if len(prev) == 1:
        next_val = 0
    else:
        next_val = prev[1] - prev[0]

    if next_val in last_seen:
        old = last_seen[next_val]
        i = 1 if len(old) == 2 else 0
        last_seen[next_val] = (old[i], t)
    else:
        last_seen[next_val] = (t,)
    return next_val

last_seen = {}
for i,val in enumerate(argv[1].split(',')):
    last_seen[int(val)] = (i+1,)
    last = int(val)

for t in range(len(last_seen) + 1, 2021):
    last = do_turn(last_seen, t, last)

print('Part 1:', last)

for t in range(2021, 30_000_001):
    last = do_turn(last_seen, t, last)

print('Part 2:', last)
