#!/usr/bin/env python3
from sys import argv

def transform(public_key, loop_val):
    val = 1
    for _ in range(loop_val):
        val = (public_key * val) % 20201227
    return val

filename = argv[1]
with open(filename) as f:
    card, door = [int(x) for x in f.readlines()]

# find one of the loop keys
subj = 7
val = 1
loop = 1
while True:
    val = (subj * val) % 20201227
    if val == card:
        print('Part 1:', transform(door, loop))
        break
    elif val == door:
        print('Part 1:', transform(card, loop))
        break
    else:
        loop += 1
