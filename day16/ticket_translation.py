#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
from constraint import *
import re

def valid_tag(rules, tag):
    valids = []
    for k,ranges in rules.items():
        for r in ranges:
            start, end = r
            if start <= tag <= end:
                valids.append(k)
                break
    return set(valids)

filename = argv[1]
state = 'rules'
rules = defaultdict(list)
tot = 0
constraints = {}
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        if line == 'your ticket:':
            state = 'ticket'
            for k in rules:
                constraints[k] = set(range(len(rules)))
        elif line == 'nearby tickets:':
            state = 'nearby'
        elif state == 'rules':
            k = line.split(':')[0]
            m = re.findall('(\d+)-(\d+)', line)
            for start, end in m:
                rules[k].append((int(start),int(end)))
        elif state == 'ticket':
            ticket = [int(x) for x in line.split(',')]
            state = ''
        elif state == 'nearby':
            tags = [int(x) for x in line.split(',')]
            for i in range(len(tags)):
                tag = tags[i]
                valids = valid_tag(rules, tag)
                if not valids:
                    tot += tag
                else:
                    for k in rules:
                        if k not in valids:
                            constraints[k].remove(i)

print('Part 1: ', tot)

problem = Problem()
problem.addConstraint(AllDifferentConstraint())
for k,v in constraints.items():
    problem.addVariable(k, list(v))
prod = 1
for solution in problem.getSolutions():
    for k,v in solution.items():
        if k.startswith('departure'):
            prod *= ticket[v]
print('Part 2:', prod)

        
