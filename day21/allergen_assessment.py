#!/usr/bin/env python3
from sys import argv
import re
from constraint import *

ingredients = ["dairy",
               "eggs",
               "fish",
               "nuts",
               "peanuts",
               "sesame",
               "shellfish",
               "soy",
]
ingred_no = {v:(1<<i) for (i,v) in enumerate(ingredients)}
ingred_no['blank'] = 0
print(f'{ingred_no}')

def all_diff_nonzero(*args):
    print(f'all_diff_nonzero {args=}')
    seen = set()
    for a in args:
        if a > 0:
            if a in seen:
                return False
            else:
                seen.add(a)
    return True

def sum_to(*args):
#    return sum(args) == 255
    print(f'sum_to {args=}')
    return sum(args) == ingred_no['dairy'] + ingred_no['fish'] + ingred_no['soy']

def make_constraint(p, f, i):
    mask = sum([ingred_no[k] for k in i])
    l = f'lambda {",".join(f)}: ({" + ".join(f)}) & {mask} == {mask}'
    print(l, f)
    p.addConstraint(eval(l), f)

foods = {}
problem = Problem()
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        fields = line.split(' (')
        m = re.search('contains (.*)\)', fields[1])
        i = m.group(1).split(', ')
        f = fields[0].split(' ')
        for fd in f:
            if fd not in foods:
                foods[fd] = set([0])
#                problem.addVariable(fd, list(ingred_no.values()))
            for ing in i:
                foods[fd].add(ingred_no[ing])
        
print(f'{len(foods)=}')
print(f'{foods=}')
print(f'{list(foods)}')
for fd in foods:
    problem.addVariable(fd, list(foods[fd]))
    
problem.addConstraint(FunctionConstraint(all_diff_nonzero), foods.keys())
problem.addConstraint(FunctionConstraint(sum_to), foods.keys())

with open(filename) as f:
    for line in f:
        line = line.rstrip()
        fields = line.split(' (')
        f = fields[0].split(' ')
        m = re.search('contains (.*)\)', fields[1])
        i = m.group(1).split(', ')
        print(f'{i=}')
        make_constraint(problem, f, i)

print(problem.getSolutions())
