#!/usr/bin/env python3
from sys import argv

N = 1_000_000
MOVES = 10_000_000

class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next_node = None

def create_circle_list(cups):
    d = {}
    arr = [int(c) for c in cups]
    for i in arr:
        d[i] = LinkedList(i)

    for i in range(10,N+1):
        d[i] = LinkedList(i)

    for i in range(len(arr)-1):
        d[arr[i]].next_node = d[arr[(i+1) % len(arr)]]

    # d[arr[8]].next_node = d[arr[0]]
    d[arr[8]].next_node = d[10]
    for i in range(10, N):
        d[i].next_node = d[i+1]
    d[N].next_node = d[arr[0]]
    
    return d[arr[0]], d

def do_move(clist, d):
    # bypass the next 3 nodes
    front = clist.next_node
    back = front.next_node.next_node
    clist.next_node = back.next_node

    # which vals were just picked?
    picked = [front.val, front.next_node.val, front.next_node.next_node.val]

    # find the destination node num
    dest = clist.val - 1
    if dest == 0:
        dest = N
    while dest in picked:
        dest = dest - 1
        if dest == 0:
            dest = N

    # find the destination node
    p = d[dest]

    # insert the picked nodes at p
    back.next_node = p.next_node
    p.next_node = front

def compute_score(clist):
    s = ''

    # find 1
    while clist.val != 1:
        clist = clist.next_node

    # find the next 2 vals
    x = clist.next_node.val
    y = clist.next_node.next_node.val
    print(f'{x=} {y=}')
    return x * y

clist, d = create_circle_list(argv[1])
# tmp = clist
# for _ in range(N):
#     print(tmp.val)
#     tmp = tmp.next_node

for move in range(MOVES):
    if move % 100_000 == 0:
        print(f'{move=}')
    do_move(clist, d)
    clist = clist.next_node
    # print(f'{move=}  ', end='')
    # tmp = clist
    # for _ in range(N):
    #     print(f'{tmp.val} ', end='')
    #     tmp = tmp.next_node
    # print()

# compute score
print('Part 2:', compute_score(clist))
