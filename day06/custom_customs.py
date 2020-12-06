#!/usr/bin/env python3
from sys import argv

questions = set()
num_groups = 0
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        if line:
            for q in line:
                questions.add(q)
        else:
            num_groups += len(questions)
            questions.clear()

print('Part 1:', num_groups)
