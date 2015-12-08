#! /usr/bin/env python

# This example we  will define a class that represents a set of items
# The set will implement the following functions with operators
#   1. union (+)
#   2. intersection (*)
#   4. contains (in)
 

class myset:

    def __init__(self, initial_items=[]):
        self.items = []

        # Add the initial items
        for i in initial_items:
            if i not in self.items:
                self.items.append(i)

    def clone(self):
        # Makes a copy
        return myset(self.items)

    def contains(self, item):
        # Returns true if item is in the set
        return (item in self.items)

    def __contains__(self, item):
        # This operator is implemented in terms of a function
        return self.contains(item)

    def union(self, other):
        # computes the union of this set and a set other
        # this function modifies the set!
        for i in other.items:
            if i not in self.items:
                self.items.append(i)

        return self

    def __add__(self, other):
        # Computes the union but does not modify the LHS or RHS
        lhs = self.clone()
        rhs = other.clone()
        return lhs.union(rhs)

    def intersect(self, other):
        # Computes the intersection of this set with a set other
        # this function modifies the set!
        common_items = []
        for i in self.items:
            if i in other:
                common_items.append(i)
        self.items = common_items
        return self
    
    def __mul__(self, other):
        # Computes the intersection but does not modify the LHS or RHS
        lhs = self.clone()
        rhs = other.clone()
        return lhs.intersect(other)

    def __str__(self):
        return str(self.items)


A = myset(range(4))
B = myset(range(2, 6))
C = A.clone()
D = B.clone()

print "A =", A
print "B =", B
print "C =", C
print "D =", D

# In operator:
print
print "3 in A:", 3 in A
print "99 in B:", 99 in B

# Using the function
A.union(B)
C.intersect(D)

print
print "A union B:", A
print "C intersect D:", C

# Using operators
A = myset(range(4))
B = myset(range(2, 6))

print
print "A + B:", A+B
print "A * B:", A*B

        
