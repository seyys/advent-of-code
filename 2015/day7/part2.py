import numpy as np
import functools

class instructions:
    @functools.cache
    def ins_and(a, b):
        return a & b
    
    @functools.cache
    def ins_or(a, b):
        return a | b

    @functools.cache
    def ins_lshift(a, val):
        return a << val

    @functools.cache
    def ins_rshift(a, val):
        return a >> val

    @functools.cache
    def ins_not(a):
        return ~a

    @functools.cache
    def ins_val(a):
        return a

class node:
    def __init__(self, instruction):
        if "AND" in instruction:
            self.ins = instructions.ins_and
            self.a, self.b = instruction.split(' AND ')
        elif "OR" in instruction:
            self.ins = instructions.ins_or
            self.a, self.b = instruction.split(' OR ')
        elif "LSHIFT" in instruction:
            self.ins = instructions.ins_lshift
            self.a, self.b = instruction.split(' LSHIFT ')
        elif "RSHIFT" in instruction:
            self.ins = instructions.ins_rshift
            self.a, self.b = instruction.split(' RSHIFT ')
        elif "NOT" in instruction:
            self.ins = instructions.ins_not
            __, self.a = instruction.split('NOT ')
            self.b = None
        else:
            try:
                int(instruction)
                self.val = lambda : np.uint16(instruction)
            except:
                self.a = instruction
                self.b = None
                self.ins = instructions.ins_val
        try:
            self.a = np.uint16(self.a)
        except:
            pass
        try:
            self.b = np.uint16(self.b)
        except:
            pass
    
    @functools.cache
    def val(self):
        if not isinstance(self.a, np.uint16):
            a = nodes[self.a].val()
        else:
            a = self.a
        if not self.b:
            return self.ins(a)

        if not isinstance(self.b, np.uint16) and self.b:
            b = nodes[self.b].val()
        else:
            b = self.b
        return self.ins(a,b)

with open('input.txt') as f:
    d = f.readlines()
    d = [x.strip() for x in d]
    d = [x.split(' -> ') for x in d]

nodes = dict()

for row in d:
    nodes[row[1]] = node(row[0])

nodes['b'] = node("46065")

print(nodes["a"].val())