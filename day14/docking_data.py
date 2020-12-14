#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
import re

mem = defaultdict(int)
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        if line[0:4] == 'mask':
            one_mask =  int(''.join(['1' if c == '1' else '0' for c in line]), 2)
            zero_mask = int(''.join(['0' if c == '0' else '1' for c in line]), 2)
        else:
            m = re.search('mem\[(\d+)\] = (\d+)', line)
            k = int(m.group(1))
            v = int(m.group(2))
            mem[k] = (v | one_mask) & zero_mask

print('Part 1:', sum(mem.values()))

