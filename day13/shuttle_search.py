#!/usr/bin/env python3
from sys import argv
from sympy.ntheory.modular import crt

filename = argv[1]
m = []
v = []
with open(filename) as f:
    start_time = int(f.readline().rstrip())
    ids_raw = f.readline().rstrip().split(',')
    ids = [int(i) for i in ids_raw if i != 'x']
    for i in range(len(ids_raw)):
        if ids_raw[i] != 'x':
            n = int(ids_raw[i])
            m.append(n)
            v.append(0 if i == 0 else n-i)

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

print('Part 2:', crt(m, v)[0])
