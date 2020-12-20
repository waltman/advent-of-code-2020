#!/usr/bin/env python3
from sys import argv
import numpy as np
import re

class Tile:
    def __init__(self, num, grid):
        self.num = num
        self.grid = grid

def parse_input(filename):
    tiles = []
    
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            if m := re.search('Tile (\d+):', line):
                num = int(m.group(1))
                grid = np.zeros([10,10], dtype=int)
                row = 0
            elif line == '':
                tiles.append(Tile(num, grid))
            else:
                for c in range(10):
                    grid[row][c] = 0 if line[c] == '.' else 1
                row += 1
    return tiles

filename = argv[1]
tiles = parse_input(filename)
for t in tiles:
    print(t.num)
    print(t.grid)
