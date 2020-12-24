#!/usr/bin/env python3
from sys import argv
from collections import defaultdict

def get_coords(line):
    r,c = 0,0
    i = 0
    while i < len(line):
        if line[i] == 'e':
            c += 2
            i += 1
        elif line[i] == 'w':
            c -= 2
            i += 1
        elif line[i:i+2] == 'nw':
            r += 1
            c -= 1
            i += 2
        elif line[i:i+2] == 'ne':
            r += 1
            c += 1
            i += 2
        elif line[i:i+2] == 'sw':
            r -= 1
            c -= 1
            i += 2
        elif line[i:i+2] == 'se':
            r -= 1
            c += 1
            i += 2
    return r,c

tiles = defaultdict(int)
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        r,c = get_coords(line)
        k = f'{r},{c}'
        tiles[k] = (tiles[k] + 1) % 2

print('Part 1:', sum(tiles.values()))

        
