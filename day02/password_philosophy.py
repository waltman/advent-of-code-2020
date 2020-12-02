#!/usr/bin/env python3
from sys import argv

def letter_count(password, letter):
    cnt = 0
    for ch in password:
        if ch == letter:
            cnt += 1
    return cnt

def is_valid(password, letter, p1, p2):
    return (password[p1-1] == letter) ^ (password[p2-1] == letter)

count1 = 0
count2 = 0
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        times, letter, password = line.split(' ')
        start, end = (int(n) for n in times.split('-'))
        letter = letter[0]
        lc = letter_count(password, letter)
        if start <= letter_count(password, letter) <= end:
            count1 += 1
        if is_valid(password, letter, start, end):
            count2 += 1

print('Part 1:', count1)
print('Part 2:', count2)
