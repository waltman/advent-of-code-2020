#!/usr/bin/env python3
from sys import argv

tree_map = []
filename = argv[1]
with open(filename) as f:
    tree_map = [line.rstrip() for line in f]

num_rows = len(tree_map)
num_cols = len(tree_map[0])

# Part 1
row, col = 0,0
dr,dc = 1,3
num_trees = 0
while row < num_rows:
    if tree_map[row][col] == '#':
        num_trees += 1

    row += dr
    col = (col + dc) % num_cols

print('Part 1:', num_trees)

