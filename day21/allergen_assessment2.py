#!/usr/bin/env python3
from sys import argv
import re
from itertools import permutations
from collections import defaultdict

ingredients = []
allergens = []
filename = argv[1]
all_allergens = set()
counts = defaultdict(int)

with open(filename) as f:
    for line in f:
        line = line.rstrip()

        # parse the ingredients
        m = re.search('^(.*) \(', line)
        ingredients.append(m.group(1).split(' '))
        for ing in ingredients[-1]:
            counts[ing] += 1

        # parse the allergens
        m = re.search('contains (.*)\)', line)
        allergens.append(m.group(1).split(', '))
        for allerg in allergens[-1]:
            all_allergens.add(allerg)

# perm = permutations(ingredients[0], len(allergens[0]))
# for p in perm:
#     print(p)
stack = [(permutations(ingredients[0], len(allergens[0])), allergens[0], 0, {})]
while (stack):
    perm, allerg, level, assign = stack[-1]
    try:
        p = next(perm)
    except StopIteration:
        stack.pop()
        continue

#    print(f'{level=} {p=} {assign=}')
    conflict = False
    # assign this permutation to the allergens
    new_assign = assign.copy()
    rev_assign = {v: k for k,v in new_assign.items()}
    for i in range(len(p)):
        if (allerg[i] in new_assign and new_assign[allerg[i]] != p[i]) or (p[i] in rev_assign and rev_assign[p[i]] != allerg[i]):
            # bad perm, skip
#            print('bad perm')
            conflict = True
            break
        else:
            new_assign[allerg[i]] = p[i]
    if conflict:
        continue

    # does this break any of the later rules?
    for lev in range(level+1, len(ingredients)):
        if conflict:
            break
        for k,v in new_assign.items():
            if k in allergens[lev] and v not in ingredients[lev]:
#                print(f'conflict at {lev=}: {v=} {k=}')
                conflict = True
                break

    if conflict:
#        print('found conflict, continuing')
        continue
    elif len(new_assign) == len(all_allergens):
        print('found a solution!')
        print(new_assign)
        break
    else:
#        print('recursing!')
        # find a level with unused allergens
        found = False
        for lev in range(level+1, len(allergens)):
            if found:
                break
            for allerg in allergens[lev]:
                if allerg not in new_assign:
                    stack.append((permutations(ingredients[lev], len(allergens[lev])), allergens[lev], lev, new_assign))
                    found = True
                    break

print(new_assign)
tot = 0
used = set(new_assign.values())
print(f'{used=}')
for k,v in counts.items():
    if k not in used:
        print(f'{k=} {v=}')
        tot += v
print('Part 1:', tot)

part2 = []
for k in sorted(new_assign):
    part2.append(new_assign[k])
print('Part 2:', ','.join(part2))
