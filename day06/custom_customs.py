#!/usr/bin/env python3
from sys import argv
from collections import defaultdict

questions = defaultdict(int)
num_groups = 0
num_all = 0
group_size = 0
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        if line:
            group_size += 1
            for q in line:
                questions[q] += 1
        else:
            num_groups += len(questions)
            # how many questions did everyone answer?
            num_all += len([v for v in questions.values() if v == group_size])

            questions.clear()
            group_size = 0

print('Part 1:', num_groups)
print('Part 2:', num_all)
