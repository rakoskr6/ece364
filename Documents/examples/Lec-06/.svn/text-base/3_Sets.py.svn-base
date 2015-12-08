#! /usr/bin/env python

#   $Author: ee364 $
#     $Date: 2001/09/21 16:04:32 $
# $Revision: 1.2 $

import sys

print """
The system search path

A = sys.path
for I in range(0, len(A)):
    print repr (A[I])
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

A = sys.path
for I in range(0, len(A)):
    print repr (A[I])

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print """
The system path can be extended by appending
new directories to the list.

sys.path.append('/a/ee364/LEC-06')
A = sys.path
for I in range(0, len(A)):
    print repr (A[I])
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

sys.path.append('/a/ee364/LEC-06')
A = sys.path
for I in range(0, len(A)):
    print repr (A[I])

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------



print """
import Pro_Set

def Main():
    A = [1, 2, 3, 4, 5]
    B = [3, 4, 5, 6, 7]
    print "A: ", A
    print "B: ", B
    C = Pro_Set.Intersection(A, B)
    print "C = A intersection B:", C
    D = Pro_Set.Union(A, B)
    print "D = A union B:", D

Main()
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

import Pro_Set

def Main():
    A = [1, 2, 3, 4, 5]
    B = [3, 4, 5, 6, 7]
    print "A: ", A
    print "B: ", B
    C = Pro_Set.Intersection(A, B)
    print "C = A intersection B:", C
    D = Pro_Set.Union(A, B)
    print "D = A union B:", D

Main()

