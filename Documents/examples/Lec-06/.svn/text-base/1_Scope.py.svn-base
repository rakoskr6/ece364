#! /usr/bin/env python

#   $Author: ee364 $
#     $Date: 2001/02/26 21:15:51 $
# $Revision: 1.2 $

import sys

print """
This program looks at the scoping of
data in functions
"""

print """
A is a local variable in Change ()

def Change ():
     A = "Big Deal"
     print "In Change A: ", A
     return

A = 5
print "Before call A: ", A
Change()
print " After call A: ", A
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

def Change ():
     A = "Big Deal"
     print "In Change A: ", A
     return

A = 5
print "Before call A: ", A
Change()
print " After call A: ", A

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print """
A is a global variable in Change ()

def Change ():
     global A
     A = "Big Deal"
     print "In Change A: ", A
     return

A = 5
print "Before call A: ", A
Change()
print " After call A: ", A
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

def Change ():
     global A
     A = "Big Deal"
     print "In Change A: ", A
     return

A = 5
print "Before call A: ", A
Change()
print " After call A: ", A

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print """
A is a local to Change () and returned

def Change ():
     A = "Big Deal"
     print "In Change A: ", A
     return A

A = 5
print "Before call A: ", A
A = Change()
print " After call A: ", A
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print


# ************************************************

def Change ():
     A = "Big Deal"
     print "In Change A: ", A
     return A

A = 5
print "Before call A: ", A
A = Change()
print " After call A: ", A

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print """
A is passed by reference to Change ()

def Change (X):
     X = "Big Deal"
     print "In Change X: ", X
     return

A = 5
print "Before call A: ", A
Change(A)
print " After call A: ", A
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print


# ************************************************

def Change (X):
     X = "Big Deal"
     print "In Change X: ", X
     return

A = 5
print "Before call A: ", A
Change(A)
print " After call A: ", A

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print """
A is passed by reference to Change ()
A is local to Change ()

def Change (A):
     A = "Big Deal"
     print "In Change A: ", A
     return

A = 5
print "Before call A: ", A
Change(A)
print " After call A: ", A
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

def Change (A):
     A = "Big Deal"
     print "In Change A: ", A
     return

A = 5
print "Before call A: ", A
Change(A)
print " After call A: ", A

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print """
A is passed by reference to Change ()
A is both local and global to Change ()

THIS IS NOT LEGAL AND WILL NOT RUN 

def Change (A):
     global A
     A = "Big Deal"
     print "In Change A: ", A
     return

A = 5
print "Before call A: ", A
Change(A)
print " After call A: ", A
"""

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print """
X and Y are global in scope in Add_Items

def Add_Items():
     Sum = X + Y
     return Sum

X = 2.0
Y = 3.0
Z = "Big Deal"
print "Before X: ", X
print "Before Y: ", Y
print "Before Z: ", Z
Z = Add_Items()
print " After X: ", X
print " After Y: ", Y
print " After Z: ", Z
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

def Add_Items():
     Sum = X + Y
     return Sum

X = 2.0
Y = 3.0
Z = "Big Deal"
print "Before X: ", X
print "Before Y: ", Y
print "Before Z: ", Z
Z = Add_Items()
print " After X: ", X
print " After Y: ", Y
print " After Z: ", Z

sys.exit(0)
