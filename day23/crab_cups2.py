#!/usr/bin/env python3
from sys import argv

class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next_node = None

def create_circle_list(cups):
    d = {}
    a = [int(c) for c in cups]
    for i in a:
        d[i] = LinkedList(i)

    for i in range(len(a)):
        d[a[i]].next_node = d[a[(i+1) % len(a)]]

    return d[a[0]]        

def do_move(clist):
    # bypass the next 3 nodes
    front = clist.next_node
    back = front.next_node.next_node
    clist.next_node = back.next_node

    # which vals were just picked?
    picked = set([front.val, front.next_node.val, front.next_node.next_node.val])

    # find the destination node num
    dest = clist.val - 1
    if dest == 0:
        dest = 9
    while dest in picked:
        dest = dest - 1
        if dest == 0:
            dest = 9

    # find the destination node
    p = clist.next_node
    while p.val != dest:
        p = p.next_node

    # insert the picked nodes at p
    back.next_node = p.next_node
    p.next_node = front

def compute_score(clist):
    s = ''

    # find 1
    while clist.val != 1:
        clist = clist.next_node

    # find all the non-1s
    while True:
        clist = clist.next_node
        if clist.val == 1:
            break
        else:
            s += str(clist.val)
    return s

clist = create_circle_list(argv[1])

for move in range(100):
    do_move(clist)
    clist = clist.next_node
    print(f'{move=}  ', end='')
    tmp = clist
    for _ in range(len(argv[1])):
        print(f'{tmp.val} ', end='')
        tmp = tmp.next_node
    print()

# compute score
print('Part 1:', compute_score(clist))


