#!/usr/bin/env python3
from sys import argv

def letter_count(password, letter):
    cnt = 0
    for ch in password:
        if ch == letter:
            cnt += 1
    return cnt

count = 0
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        times, letter, password = line.split(' ')
        start, end = (int(n) for n in times.split('-'))
        letter = letter[0]
        lc = letter_count(password, letter)
        if start <= letter_count(password, letter) <= end:
            count += 1

print('Part 1:', count)
        
