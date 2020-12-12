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
        
class Waypoint(Navigate):
    def __init__(self):
        Navigate.__init__(self)
        self.waypoint = [1,10]
        
    def move(self, action, value):
        if action == 'N':
            self.waypoint[0] += value
        elif action == 'S':
            self.waypoint[0] -= value
        elif action == 'E':
            self.waypoint[1] += value
        elif action == 'W':
            self.waypoint[1] -= value
        elif action == 'F':
            self.pos[0] += value * self.waypoint[0]
            self.pos[1] += value * self.waypoint[1]
        elif action == 'R':
            self.turn_right(value)
        elif action == 'L':
            self.turn_left(value)

    def turn_right(self, value):
        if value == 90:
            self.waypoint = [-self.waypoint[1], self.waypoint[0]]
        elif value == 180:
            self.waypoint = [-self.waypoint[0], -self.waypoint[1]]
        elif value == 270:
            self.waypoint = [self.waypoint[1], -self.waypoint[0]]
        
    def turn_left(self, value):
        if value == 90:
            self.waypoint = [self.waypoint[1], -self.waypoint[0]]
        elif value == 180:
            self.waypoint = [-self.waypoint[0], -self.waypoint[1]]
        elif value == 270:
            self.waypoint = [-self.waypoint[1], self.waypoint[0]]
        
nav = Navigate()
wp = Waypoint()
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        action = line[0]
        value = int(line[1:])
        nav.move(action, value)
        wp.move(action, value)

print('Part 1:', nav.dist())
print('Part 2:', wp.dist())
