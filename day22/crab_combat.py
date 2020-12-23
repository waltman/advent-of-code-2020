#!/usr/bin/env python3
from sys import argv
from collections import deque

def score(q):
    val = len(q)
    tot = 0
    for c in q:
        tot += c * val
        val -= 1
    return tot

p1 = deque()
p2 = deque()
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        if line == 'Player 1:':
            state = 'p1'
        elif line == 'Player 2:':
            state = 'p2'
        elif line != '':
            if state == 'p1':
                p1.append(int(line))
            else:
                p2.append(int(line))

# play the game
while len(p1) and len(p2):
    c1 = p1.popleft()
    c2 = p2.popleft()
    if c1 > c2:
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c2)
        p2.append(c1)

if len(p1):
    print(f'{p1=}')
    print('Part 1:', score(p1))
else:
    print(f'{p2=}')
    print('Part 1:', score(p2))
