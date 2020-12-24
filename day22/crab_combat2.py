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

def play(p1, p2):
    seen = set()
    while len(p1) and len(p2):
        k = str(list(p1)) + str(list(p2))
        if k in seen:
            return p1, None
        else:
            seen.add(k)

        c1 = p1.popleft()
        c2 = p2.popleft()

        # play subgame?
        if c1 <= len(p1) and c2 <= len(p2):
            new_p1, new_p2 = play(deque(list(p1)[:c1]), deque(list(p2)[:c2]))
            if new_p1:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        else:
            if c1 > c2:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)

    return p1, p2

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
new_p1, new_p2 = play(p1.copy(), p2.copy())

if len(new_p1):
    print(f'{new_p1=}')
    print('Part 2:', score(new_p1))
else:
    print(f'{new_p2=}')
    print('Part 2:', score(new_p2))
