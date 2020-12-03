#!/usr/bin/env python3
from sys import argv

def num_trees(tree_map, num_rows, num_cols, dr, dc):
    trees = 0
    row,col = 0,0

    while row < num_rows:
        if tree_map[row][col] == '#':
            trees += 1

        row += dr
        col = (col + dc) % num_cols

    return trees

tree_map = []
filename = argv[1]
with open(filename) as f:
    tree_map = [line.rstrip() for line in f]

num_rows = len(tree_map)
num_cols = len(tree_map[0])

# Part 1
dr,dc = 1,3
print('Part 1:', num_trees(tree_map, num_rows, num_cols, dr, dc))

# Part 2
slopes = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2],
]

tree_prod = 1
for slope in slopes:
    dc,dr = slope
    tree_prod *= num_trees(tree_map, num_rows, num_cols, dr, dc)

print('Part 2:', tree_prod)
