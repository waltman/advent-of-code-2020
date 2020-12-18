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

filename = argv[1]
tot = 0
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        orig_line = line
        while True:
            new_line = re.sub('\(([^()]+)\)', expand_parens, line, count=1)
#            print(line, '->', new_line)
            if new_line == line:
                break
            else:
                line = new_line
        res = eval_rl(new_line)
        tot += res
#        print(orig_line, '=', res)
        
print('Part 1', tot)
