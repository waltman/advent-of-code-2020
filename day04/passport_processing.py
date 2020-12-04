#!/usr/bin/env python3
from sys import argv
from copy import deepcopy
import re

def valid_hgt(v):
    if v[-2:] == 'cm':
        return 150 <= int(v[0:-2]) <= 193
    elif v[-2:] == 'in':
        return 59 <= int(v[0:-2]) <= 76
    else:
        return False

VALID = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}

valid_field = {
    'byr': lambda v : 1920 <= int(v) <= 2002,
    'iyr': lambda v : 2010 <= int(v) <= 2020,
    'eyr': lambda v : 2020 <= int(v) <= 2030,
    'hgt': valid_hgt,
    'hcl': lambda v : re.match('#[0-9a-f]{6}', v),
    'ecl': lambda v : v in {'amb','blu','brn','gry','grn','hzl','oth'},
    'pid': lambda v : re.match('^\d{9}$', v),
    'cid': lambda v : True,
}

num_valid = 0
num_valid2 = 0
filename = argv[1]
with open(filename) as f:
    missing = deepcopy(VALID)
    ok = True
    for line in f:
        line = line.rstrip()
        if line:
            m = re.findall('(.{3}):([^ ]+)', line)
            for k,v in m:
                missing.remove(k)
                if not valid_field[k](v):
                    ok = False
        else:
            if missing == set() or missing == {'cid'}:
                num_valid += 1
                if ok:
                    num_valid2 += 1
            missing = deepcopy(VALID)
            ok = True

print('Part 1:', num_valid)
print('Part 2:', num_valid2)

