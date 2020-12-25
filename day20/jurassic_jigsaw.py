#!/usr/bin/env python3
from sys import argv
import numpy as np
import re
from collections import defaultdict
import networkx as nx

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

    def shared_edge(self, tile):
        mine = set(self.edges())
        theirs = set(tile.edges())
        return mine & theirs

def parse_input(filename):
    tiles = {}
    
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            if m := re.search('Tile (\d+):', line):
                num = int(m.group(1))
                grid = np.zeros([10,10], dtype=int)
                row = 0
            elif line == '':
                tiles[num] = Tile(num, grid)
            else:
                for c in range(10):
                    grid[row][c] = 0 if line[c] == '.' else 1
                row += 1
    return tiles

def find_neighbors(tiles):
    neighbors = defaultdict(set)
    for t in tiles:
        for e in t.edges():
            neighbors[e].add(t.num)
    return [n for n in neighbors.values() if len(n) == 2]

def num_neighbors(neighbors):
    neighs = defaultdict(int)
    for s in neighbors:
        for n in s:
            neighs[n] += 1
    return neighs

filename = argv[1]
tiles = parse_input(filename)

neighbors = find_neighbors(tiles.values())
print('neigbors =', neighbors)
neighs = num_neighbors(neighbors)
prod = 1
for n in neighs:
    if neighs[n] == 4:
        prod *= n
print('Part 1:', prod)
N = int(len(tiles)**0.5)
print(f'{N=}')
corners = {n for n in neighs if neighs[n] == 4}
print(corners)
print(list(corners)[0])

G = nx.Graph()
for n in neighbors:
    nl = list(n)
    G.add_edge(nl[0], nl[1])

# Slot the tiles into the image
image = [[0 for i in range(N)] for j in range(N)]

# Add the corners
corner_list = list(corners)
image[0][0] = corner_list[0]
for i in range(1,4):
    if len(nx.shortest_path(G, corner_list[0], corner_list[i])) == N:
        if image[0][N-1] == 0:
            image[0][N-1] = corner_list[i]
        else:
            image[N-1][0] = corner_list[i]
    else:
        image[N-1][N-1] = corner_list[i]

# first row
path = nx.shortest_path(G, image[0][0], image[0][N-1])
for i in range(1, N-1):
    image[0][i] = path[i]

# first col
path = nx.shortest_path(G, image[0][0], image[N-1][0])
for i in range(1, N-1):
    image[i][0] = path[i]

# last col
path = nx.shortest_path(G, image[0][N-1], image[N-1][N-1])
for i in range(1, N-1):
    image[i][N-1] = path[i]

# rows 1 through N-1
for r in range(1, N):
    path = nx.shortest_path(G, image[r][0], image[r][N-1])
    for i in range(1, N-1):
        image[r][i] = path[i]

print(image)

# set image to the example to test alignment
image = [[1951, 2311, 3079], [2729, 1427, 2473], [2971, 1489, 1171]]
print(image)

# line up the top row
for c in range(N-1):
    print(f'{image[0][c]=} {tiles[image[0][c]].edges()=}')
    shared = tiles[image[0][c]].shared_edge(tiles[image[0][c+1]])
    print(f'{c=} {shared=}')
    
