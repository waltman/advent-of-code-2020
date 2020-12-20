#!/usr/bin/env python3
from sys import argv
import numpy as np
import re
from collections import defaultdict

def array2bin(a):
    return int(''.join([str(c) for c in a]), 2)

class Tile:
    def __init__(self, num, grid):
        self.num = num
        self.grid = grid

    def edges(self):
        return [array2bin(a) for a in [self.grid[0], np.flip(self.grid[0]),
                                       self.grid[9], np.flip(self.grid[9]),
                                       self.grid[:,0], np.flip(self.grid[:,0]),
                                       self.grid[:,9], np.flip(self.grid[:,9])]]

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
edges = defaultdict(int)
for t in tiles:
#    print(t.num)
#    print(t.grid)
#    print(t.edges())
    for e in t.edges():
        edges[e] += 1
print(edges)
cnts = defaultdict(int)
for v in edges.values():
    cnts[v] += 1
print(cnts)

    
