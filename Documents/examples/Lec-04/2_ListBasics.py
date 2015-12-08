#! /usr/bin/env python

import sys

# Generate some lists of numbers
A = range(10)
B = range(5,11)
C = range(10,100,10)

# D is a list that contains 3 lists
D = [A, B, C]

print "List A:"
print "\tlength: %d" % (len(A),)
print "\titems:", A

print "List B:"
print "\tlength: %d" % (len(B),)
print "\titems:", B

print "List C:"
print "\tlength: %d" % (len(C),)
print "\titems:", C

print "List D:"
print "\tlength: %d" % (len(D),)
print "\titems:", D

# Indexing a list
print
print "D[1] is ", D[1]
print "D[1][2] is ", D[1][2]
print "D[0][-2] is ", D[0][-2]

print

# Appending to a list
E = [0,0,0]
D.append(E)

print D

F = range(1,4)

# Notice that each element of F will be added to D
D += F

print D

# Notice that the entire list is added as a single element to D
D += [F]

print D

print

# Converting a list to a tuple

A_tuple = tuple(A)
B_tuple = tuple(B)
print A_tuple, B_tuple

sys.exit(0)
