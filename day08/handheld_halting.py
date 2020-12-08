#!/usr/bin/env python3
from sys import argv

class BootCode:
    def __init__(self, pgm):
        self.pgm = pgm
        self.ip = 0
        self.acc = 0
        self.ip_seen = set()

    def run(self):
        while True:
            if self.ip in self.ip_seen:
                return self.acc
            else:
                self.ip_seen.add(self.ip)

                op, arg = self.pgm[self.ip]
                if op == 'acc':
                    self.do_acc(arg)
                elif op == 'jmp':
                    self.do_jmp(arg)
                elif op == 'nop':
                    self.do_nop(arg)
                else:
                    print('unexpected op!', self.op)
                    return 0
        
    def run2(self):
        while True:
            if self.ip in self.ip_seen:
                return None
            elif self.ip == len(self.pgm):
                return self.acc
            else:
                self.ip_seen.add(self.ip)

                op, arg = self.pgm[self.ip]
                if op == 'acc':
                    self.do_acc(arg)
                elif op == 'jmp':
                    self.do_jmp(arg)
                elif op == 'nop':
                    self.do_nop(arg)
                else:
                    print('unexpected op!', self.op)
                    return 0
        
    def do_acc(self, arg):
        self.acc += arg;
        self.ip += 1

    def do_jmp(self, arg):
        self.ip += arg

    def do_nop(self, arg):
        self.ip += 1
        
filename = argv[1]
pgm = []
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        op, arg = line.split(' ')
        pgm.append((op, int(arg)))

bc = BootCode(pgm)
print('Part 1:', bc.run())

# Part 2
for i in range(len(pgm)):
    pgm2 = [inst for inst in pgm]
    op, arg = pgm2[i]
    if op == 'nop':
        pgm2[i] = ('jmp', arg)
        bc = BootCode(pgm2)
    elif op == 'jmp':
        pgm2[i] = ('nop', arg)
        bc = BootCode(pgm2)
    else:
        bc = None

    if bc:
        result = bc.run2()
        if result is not None:
            print('Part 2:', result)
            break

