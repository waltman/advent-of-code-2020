#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
from itertools import product
from copy import deepcopy
import re

def mask_addrs(mask, addr):
    template = []
    xpos = []
    for i, m in enumerate(mask):
        if m == '0':
            template.append('1' if addr & 1<<(35-i) else '0')
        elif m == '1':
            template.append('1')
        else:
            template.append('X')
            xpos.append(i)

    for p in product('01', repeat=len(xpos)):
        t = deepcopy(template)
        for i in range(len(p)):
            t[xpos[i]] = p[i]
        yield int(''.join(t), 2)

mem = defaultdict(int)
mem2 = defaultdict(int)
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        if line[0:4] == 'mask':
            mask = line.split(' = ')[1]
            one_mask =  int(''.join(['1' if c == '1' else '0' for c in mask]), 2)
            zero_mask = int(''.join(['0' if c == '0' else '1' for c in mask]), 2)
        else:
            m = re.search('mem\[(\d+)\] = (\d+)', line)
            k = int(m.group(1))
            v = int(m.group(2))
            mem[k] = (v | one_mask) & zero_mask
            for addr in mask_addrs(mask, k):
                mem2[addr] = v

print('Part 1:', sum(mem.values()))
print('Part 2:', sum(mem2.values()))
