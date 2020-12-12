#!/usr/bin/env python3
from sys import argv

class Navigate:
    next_right = {
        ( 0, 1): (-1, 0),
        (-1, 0): ( 0,-1),
        ( 0,-1): ( 1, 0),
        ( 1, 0): ( 0, 1),
    }

    next_left = {
        ( 0, 1): ( 1, 0),
        ( 1, 0): ( 0,-1),
        ( 0,-1): (-1, 0),
        (-1, 0): ( 0, 1),
    }        

    def __init__(self):
        self.pos = [0,0]
        self.direction = 0,1
        
    def dist(self):
        return abs(self.pos[0]) + abs(self.pos[1])

    def move(self, action, value):
        if action == 'N':
            self.pos[0] += value
        elif action == 'S':
            self.pos[0] -= value
        elif action == 'E':
            self.pos[1] += value
        elif action == 'W':
            self.pos[1] -= value
        elif action == 'F':
            self.pos[0] += value * self.direction[0]
            self.pos[1] += value * self.direction[1]
        elif action == 'R':
            self.turn_right(value)
        elif action == 'L':
            self.turn_left(value)

    def turn_right(self, value):
        for _ in range(value // 90):
            self.direction = self.next_right[self.direction]
        
    def turn_left(self, value):
        for _ in range(value // 90):
            self.direction = self.next_left[self.direction]
        
nav = Navigate()
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        action = line[0]
        value = int(line[1:])
        nav.move(action, value)

print('Part 1:', nav.dist())
