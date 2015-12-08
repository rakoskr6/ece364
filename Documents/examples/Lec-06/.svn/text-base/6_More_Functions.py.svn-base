#! /usr/bin/env python

#   $Author: ee364 $
#     $Date: 2001/02/22 20:01:06 $
# $Revision: 1.1 $

import sys

print """
functions can be assigned to variables and also
passed to functions

import math
import cmath

def Doit (X, Y):
    return Y(X)

Function = math.sin
print Function(2.0)
print Doit (2.0, Function)

Function = math.exp
print Function(2.0)
print Doit (2.0, Function)

print cmath.sqrt(-2.0)
print Doit (-2.0, cmath.sqrt)
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

import math
import cmath

def Doit (X, Y):
    return Y(X)

Function = math.sin

Function = math.sin
print Function(2.0)
print Doit (2.0, Function)
print
Function = math.exp
print Function(2.0)
print Doit (2.0, Function)
print
print cmath.sqrt(-2.0)
print Doit (-2.0, cmath.sqrt)

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print """
Functions can have default values
These are used if not passed to the function
They must be assigned values after all parameters
without defaults in the parameter list

def Sum (X, Y = 3, Z = 5):
    return X + Y + Z

print Sum (1, 2, 3)
print Sum (1, 2)
print Sum (1)
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

def Sum (X, Y = 3, Z = 5):
    return X + Y + Z

print Sum (1, 2, 3)
print Sum (1, 2)
print Sum (1)

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print """
Functions can handle unknown list of parameters
by using a * before the variable name
All parameters are then collected into tuble of
with the variable name

def Sum (*Data):
    Total = 0
    if len(Data) > 0:
        for I in range(0,len(Data)):
            Total = Total + Data[I]
    return Total

print Sum (1, 2, 3)
print Sum (-1, -2, -3, 7, 8)
print Sum ()
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

def Sum (*Data):
    Total = 0
    if len(Data) > 0:
        for I in range(0,len(Data)):
            Total = Total + Data[I]
    return Total

print Sum (1, 2, 3)
print Sum (-1, -2, -3, 7, 8)
print Sum ()

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print """
Parameters can be named and assigned values

def Sum (X = 0, Y = 0, Z = 0):
    return 3*X + 2*Y + Z

print Sum (Z = 3, X = 4, Y = 5)
print Sum (Y = 4, Z = 2, X = 1)
print Sum (X = 3)
print Sum (Y = 4)
print Sum (Z = 5, X = -2)
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

def Sum (X = 0, Y = 0, Z = 0):
    return 3*X + 2*Y + Z

print Sum (Z = 3, X = 4, Y = 5)
print Sum (Y = 4, Z = 2, X = 1)
print Sum (X = 3)
print Sum (Y = 4)
print Sum (Z = 5, X = -2)

sys.exit(0)
