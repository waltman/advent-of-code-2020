#!/usr/bin/env python3
from sys import argv
from copy import deepcopy

def read_grid(filename):
    grid = []
    cols = 0
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            if cols == 0:
                cols = len(line) + 2
                s = '.' * cols
                grid.append([c for c in s])
            s = '.' + line + '.'
            grid.append([c for c in s])
    s = '.' * cols
    grid.append([c for c in s])
    return grid

def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()

def num_occupied(grid, row, col):
    adj = [(-1,-1), (-1,0), (-1,1),
           ( 0,-1),         ( 0,1),
           ( 1,-1), ( 1,0), ( 1,1),
    ]
    tot = 0
    for p in adj:
        if grid[row+p[0]][col+p[1]] == '#':
            tot += 1
    return tot

filename = argv[1]
grid = read_grid(filename)
rows = len(grid)
cols = len(grid[0])
#print_grid(grid)

while True:
    new_grid = deepcopy(grid)
    num_changed = 0
    for row in range(1,rows-1):
        for col in range(1,cols-1):
            n = num_occupied(grid, row, col)
            if grid[row][col] == 'L' and n == 0:
                new_grid[row][col] = '#'
                num_changed += 1
            elif grid[row][col] == '#' and n >= 4:
                new_grid[row][col] = 'L'
                num_changed += 1
#    print_grid(new_grid)
    if num_changed == 0:
        break
    else:
        grid = deepcopy(new_grid)

cnt = 0
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == '#':
            cnt += 1
print('Part 1:', cnt)
