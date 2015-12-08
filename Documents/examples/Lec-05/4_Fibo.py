#! /usr/bin/env python

#   $Author: ee364 $
#     $Date: 2001/10/03 00:56:47 $
# $Revision: 1.1 $


import sys
import time

print """
   This program calculates the 
   30th, 20th, and 10th Fibonacci numbers
    Fibr does it recursively
    Fibi does it iteratively
    Fibd does it recursively using dictonaries
    each routine is timed

"""
print """
       F(0) = 0
       F(1) = 1
       F(N) = F(N-1) + F(N-2)
           for  N > 0 

def Fibr (N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        Value = Fibr(N-1) + Fibr(N-2)
        return Value

for I in  [30, 20, 10]:
    Start = time.time()
    Value = Fibr(I)
    Stop = time.time()
    print "I: %2d, Fibr(%2d): %7d %6.3f seconds" % 
      (I, I, Value, (Stop - Start))
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

def Fibr (N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        Value = Fibr(N-1) + Fibr(N-2)
        return Value

for I in  [30, 20, 10]:
    Start = time.time()
    Value = Fibr(I)
    Stop = time.time()
    print "I: %2d, Fibr(%2d): %7d %6.3f seconds" % \
      (I, I, Value, (Stop - Start))

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# -------------------------------------------------

print """
       F(0) = 0
       F(1) = 1
       F(N) = F(N-1) + F(N-2)
           for  N > 0 

def Fibi (N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        F_2 = 0
        F_1 = 1
        for I in range(2,N+1):
           F = F_1 + F_2
           F_2 = F_1
           F_1 = F
    return F

for I in  [30, 20, 10]:
    Start = time.time()
    Value = Fibi(I)
    Stop = time.time()
    print "I: %2d, Fibi(%2d): %7d %6.3f seconds" % 
      (I, I, Value, (Stop - Start))
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

def Fibi (N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        F_2 = 0
        F_1 = 1
        for I in range(2,N+1):
           F = F_1 + F_2
           F_2 = F_1
           F_1 = F
    return F

for I in  [30, 20, 10]:
    Start = time.time()
    Value = Fibi(I)
    Stop = time.time()
    print "I: %2d, Fibi(%2d): %7d %6.3f seconds" % \
      (I, I, Value, (Stop - Start))

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# -------------------------------------------------

print """

def Fibd (N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        if Fibo_Cache.has_key((N)):
            return Fibo_Cache[(N)]
        else:
           Result = Fibd(N-1) + Fibd(N-2)
           Fibo_Cache[(N)] = Result
           return Result

Fibo_Cache = {}

for I in  [30, 20, 10]:
    Start = time.time()
    Value = Fibd(I)
    Stop = time.time()
    print "I: %2d, Fibd(%2d): %7d %6.3f seconds" % 
      (I, I, Value, (Stop - Start))
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

def Fibd (N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        if Fibo_Cache.has_key((N)):
            return Fibo_Cache[(N)]
        else:
           Result = Fibd(N-1) + Fibd(N-2)
           Fibo_Cache[(N)] = Result
           return Result

Fibo_Cache = {}

for I in  [30, 20, 10]:
    Start = time.time()
    Value = Fibd(I)
    Stop = time.time()
    print "I: %2d, Fibd(%2d): %7d %6.3f seconds" % \
      (I, I, Value, (Stop - Start))


print "Fibo_Cache"
print Fibo_Cache
sys.exit(0)
