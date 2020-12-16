#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
import re

def valid_tag(rules, tag):
    for k,ranges in rules.items():
        for r in ranges:
            start, end = r
            if start <= tag <= end:
                return True
    return False

filename = argv[1]
state = 'rules'
rules = defaultdict(list)
tot = 0
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        if line == 'your ticket:':
            state = 'ticket'
        elif line == 'nearby tickets:':
            state = 'nearby'
        elif state == 'rules':
            k = line.split(':')[0]
            m = re.findall('(\d+)-(\d+)', line)
            for start, end in m:
                rules[k].append((int(start),int(end)))
        elif state == 'nearby':
            tags = [int(x) for x in line.split(',')]
            for tag in tags:
                if not valid_tag(rules, tag):
                    tot += tag

print('Part 1: ', tot)
