#! /usr/bin/env python

import sys

# Generate some lists of numbers
A = range(10)
B = tuple(range(5,11))
C = "Michael Goldfarb"

print A, B, C

print "A[1:3] = ", A[1:3]
print "B[2:] = ", B[2:]
print "C[:8] = ", C[:8]


sys.exit(0)
