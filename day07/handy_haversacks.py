#!/usr/bin/env python3
from sys import argv
from collections import deque
import re

def contains_shiny_gold(rules, bag):
    queue = deque()
    queue.append(bag)
    seen = set()
    while (queue):
        bag = queue.popleft()
        if 'shiny gold' in rules[bag]:
            return True
        else:
            seen.add(bag)
            for b in rules[bag]:
                if b not in seen:
                    queue.append(b)
    return False

def bag_count(rules, bag):
    print(rules)
    print(bag, rules[bag])
    if rules[bag]:
        count = 0
        for n, b in rules[bag]:
            print(n, b)
            count += n * bag_count(rules, b)
            print(count)
        return count
    else:
        return 1

rules = dict()
rules2 = dict()
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        head, tail = line.split(' contain ')

        # parse the head
        m = re.search('^([a-z]+ [a-z]+) bag', head)
        k = m.group(1)
        if k not in rules:
            rules[k] = set()
            rules2[k] = set()

        # parse the tail
        bags = tail.split(', ')
        for bag in bags:
            m = re.search('^(\d+) ([a-z]+ [a-z]+) bag', bag)
            if m:
                rules[k].add(m.group(2))
                rules2[k].add((int(m.group(1)),m.group(2)))

num_bags = 0
for bag in rules.keys():
    if contains_shiny_gold(rules, bag):
        num_bags += 1
print('Part 1:', num_bags)

print('Part 2:', bag_count(rules2, 'shiny gold'))
