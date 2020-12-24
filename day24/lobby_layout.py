#!/usr/bin/env python3
from sys import argv

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

def neighbors(r,c):
    return [(r,c+2),
            (r,c-2),
            (r+1,c-1),
            (r+1,c+1),
            (r-1,c-1),
            (r-1,c+1)]

def rc_key(r,c):
    return f'{r},{c}'

def black_neighbors(tiles, r, c):
    cnt = 0
    for n in neighbors(r,c):
        r1,c1 = n
        cnt += tiles[rc_key(r1,c1)]
    return cnt

def run_day(tiles):
    flip = []
    for r in range(-300, 301):
        for c in range(-300, 301):
            k = rc_key(r,c)
            bn = black_neighbors(tiles, r, c)
            if tiles[k] == 1 and (bn == 0 or bn > 2):
                flip.append(k)
            elif tiles[k] == 0 and bn == 2:
                flip.append(k)
    for k in flip:
        tiles[k] = (tiles[k] + 1) % 2

tiles = {}
for r in range(-500,501):
    for c in range(-550,500):
        tiles[rc_key(r,c)] = 0
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        r,c = get_coords(line)
        k = rc_key(r,c)
        tiles[k] = (tiles[k] + 1) % 2

print('Part 1:', sum(tiles.values()))

for day in range(1, 101):
    run_day(tiles)
    if day % 10 == 0:
        print(f'Day {day}: {sum(tiles.values())}')

print('Part 2:', sum(tiles.values()))
