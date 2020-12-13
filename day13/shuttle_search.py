#!/usr/bin/env python3
from sys import argv

filename = argv[1]
with open(filename) as f:
    start_time = int(f.readline().rstrip())
    ids = [int(i) for i in f.readline().rstrip().split(',') if i != 'x']

i = 0
found = False
while not found:
    t = start_time + i
    for x in ids:
        if t % x == 0:
            print('Part 1:', i * x)
            found = True
            break
    i += 1
