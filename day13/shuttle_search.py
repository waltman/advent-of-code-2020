#!/usr/bin/env python3
from sys import argv
from sympy.ntheory.modular import crt

filename = argv[1]
with open(filename) as f:
    start_time = int(f.readline().rstrip())
    ids_raw = f.readline().rstrip().split(',')
    ids = [int(i) for i in ids_raw if i != 'x']
    v = [(int(id_raw)-i) % int(id_raw) for i, id_raw in enumerate(ids_raw) if id_raw != 'x']

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

print('Part 2:', crt(ids, v)[0])
