#!/usr/bin/env python3
from sys import argv
import re

def eval_rl(s):
    tok = s.split(' ')
    res = int(tok[0])
    for i in range(1, len(tok), 2):
        if tok[i] == '+':
            res += int(tok[i+1])
        elif tok[i] == '*':
            res *= int(tok[i+1])
        else:
            print('unexpected token:', tok[i])
        
    return res

def expand_parens(m):
    return str(eval_rl(m.group(1)))

def expand_times(m):
    return str(int(m.group(1)) * int(m.group(2)))

def expand_plus(m):
    return str(int(m.group(1)) + int(m.group(2)))

def eval2(s):
    while True:
        s2 = re.sub('(\d+) \+ (\d+)', expand_plus, s)
        if s2 == s:
            break
        else:
            s = s2
    while True:
        s3 = re.sub('(\d+) \* (\d+)', expand_times, s2)
        if s3 == s2:
            break
        else:
            s2 = s3
    return eval_rl(s3)

def expand_parens2(m):
    return str(eval2(m.group(1)))

filename = argv[1]
tot = 0
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        orig_line = line
        while True:
            new_line = re.sub('\(([^()]+)\)', expand_parens, line, count=1)
            if new_line == line:
                break
            else:
                line = new_line
        res = eval_rl(new_line)
        tot += res
        
print('Part 1', tot)

tot = 0
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        orig_line = line
        while True:
            new_line = re.sub('\(([^()]+)\)', expand_parens2, line, count=1)
            if new_line == line:
                break
            else:
                line = new_line
        res = eval2(new_line)
        tot += res
print('Part 2', tot)
