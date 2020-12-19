#!/usr/bin/env python3
from sys import argv
import re
from functools import cache

filename = argv[1]
state = 'rules'
cnt = 0
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        if state == 'rules':
            print(line)
            m = re.search('(\d+): (.*)', line)
            if m:
                ruleno = m.group(1)
                rule = m.group(2)
                if rule[0] == '"':
                    exec(f"""@cache
def rule{ruleno}(s):
    return s == {rule}""")
                elif '|' in rule:
                    m = re.search('(\d+) (\d+) \| (\d+) (\d+)', rule)
                    if m:
                        exec(f"""@cache
def rule{ruleno}(s):
    for i in range(1,len(s)):
        if (rule{m.group(1)}(s[0:i]) and rule{m.group(2)}(s[i:])) or (rule{m.group(3)}(s[0:i]) and rule{m.group(4)}(s[i:])):
            return True
    return False""")
                    else:
                        tags = rule.split(' | ')
                        exec(f"""@cache
def rule{ruleno}(s):
    return rule{tags[0]}(s) or rule{tags[1]}(s)""")
                else:
                    m = re.search('(\d+) (\d+)', rule)
                    if m:
                        exec(f"""@cache
def rule{ruleno}(s):
    for i in range(1,len(s)):
        if (rule{m.group(1)}(s[0:i]) and rule{m.group(2)}(s[i:])):
            return True
    return False""")
                    else:
                        exec(f"""@cache
def rule{ruleno}(s):
    return rule{rule}(s)""")

            else:
                state = 'messages'
        else:
            print(line, rule0(line))
            if rule0(line):
                cnt += 1

print('Part 1:', cnt)

