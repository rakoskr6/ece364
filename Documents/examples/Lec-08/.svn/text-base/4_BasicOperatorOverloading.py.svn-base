#! /usr/bin/env python

import sys, os

class SortableTuple:
    
    def __init__(self, items):
        # Rather than try to inherit directly from tuple we will implement this
        # class in terms of a tuple.
        self.values = tuple(items)

    def sort(self):
        # Member function: sorts the tuple in place
        tmp = list(self.values)
        tmp.sort()
        self.values = tuple(tmp)

    def reverse(self):
        # Member function: reverse the elements
        tmp = list(self.values)
        tmp.reverse()
        self.values = tuple(tmp)

    def __getitem__(self, index):
        # Operator "[k]": Overloads the subscript operator
        return self.values[index]

    def __contains__(self, item):
        # Operator "in": Overloads the "in" operator 
        return item in self.values

    def __len__(self):
        # Operator "len": Overloads the "len" function to support SortedTuple objects 
        return len(self.values)

    def __str__(self):
        # Operator "str": Overloads the "str" function to support SortedTuple objects
        return str(self.values)


A = range(1,10)
S = SortableTuple(A)
T = SortableTuple((7, "foo", 8, "bar"))

print "S = ", S
print "T = ", T

S.reverse()
print "Reversed: S = ", S

T.sort()
print "Sorted: T =  ", T

print "len(S) = ", len(S)

print "10 in S = ", 10 in S

print "T[2] = ", T[2]

sys.exit(0)
