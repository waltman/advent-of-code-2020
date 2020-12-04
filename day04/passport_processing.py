#!/usr/bin/env python3
from sys import argv
from copy import deepcopy
import re

VALID = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}

num_valid = 0
filename = argv[1]
with open(filename) as f:
    missing = deepcopy(VALID)
    for line in f:
        line = line.rstrip()
        if line:
            m = re.findall('(.{3}):([^ ]+)', line)
            for k,_ in m:
                missing.remove(k)
        else:
            if missing == set() or missing == {'cid'}:
                num_valid += 1
            missing = deepcopy(VALID)

print('Part 1:', num_valid)

