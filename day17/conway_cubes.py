#!/usr/bin/env python3
from sys import argv
from copy import deepcopy
import numpy as np

def read_grid(filename, n, offset):
    grid = np.zeros([n,n,n], dtype=int)
    z = n // 2
    
    with open(filename) as f:
        row = offset
        for line in f:
            line = line.rstrip()
            for i in range(len(line)):
                grid[z][row][i+offset] = 0 if line[i] == '.' else 1
            row += 1
    return grid

def neighbors(grid, z, r, c):
    return sum(sum(sum(grid[z-1:z+2,r-1:r+2,c-1:c+2])))

def cycle(grid):
    new_grid = grid.copy()
    for z in range(1, len(grid)-1):
        for r in range(1, len(grid)-1):
            for c in range(1, len(grid)-1):
                cnt = neighbors(grid, z, r, c)
                if grid[z][r][c] == 1 and (cnt < 3 or cnt > 4):
                    new_grid[z][r][c] = 0
                elif grid[z][r][c] == 0 and cnt == 3:
                    new_grid[z][r][c] = 1
    return new_grid

N = 50
OFFSET = 20
filename = argv[1]
grid = read_grid(filename, N, OFFSET)

for cyc in range(6):
    grid = cycle(grid).copy()
print('Part1:', sum(sum(sum(grid))))

