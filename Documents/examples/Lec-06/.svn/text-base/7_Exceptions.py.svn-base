#! /usr/bin/env python

#   $Author: ee364 $
#     $Date: 2001/02/22 20:01:06 $
# $Revision: 1.1 $

import sys

print """
This program looks at exception
handling in python
"""

print """
Trap on StandardError

def Open_File (File_Name):
   try:
       FILE_HANDLE = open(File_Name, "r")
   except StandardError, Message:
       print "File %s could not be opened because\\n%s\\n" \\
             % (File_Name, Message)
       FILE_HANDLE = None
   return FILE_HANDLE

HF = Open_File ("Purdue")
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

def Open_File (File_Name):
   try:
       FILE_HANDLE = open(File_Name, "r")
   except StandardError, Message:
       print "File %s could not be opened because \n%s\n" \
             % (File_Name, Message)
       FILE_HANDLE = None
   return FILE_HANDLE

HF = Open_File ("Purdue")

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print """
trap on an EnvironmentError

def Open_File (File_Name):
   try:
       FILE_HANDLE = open(File_Name, "r")
   except EnvironmentError, Message:
       print "File %s could not be opened because\\n%s\\n" \\
             % (File_Name, Message)
       FILE_HANDLE = None
   return FILE_HANDLE

HF = Open_File ("Purdue")
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

def Open_File (File_Name):
   try:
       FILE_HANDLE = open(File_Name, "r")
   except EnvironmentError, Message:
       print "File %s could not be opened because \n%s\n" \
             % (File_Name, Message)
       FILE_HANDLE = None
   return FILE_HANDLE

HF = Open_File ("Purdue")

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print """
trap on an IOError

def Open_File (File_Name):
   try:
       FILE_HANDLE = open(File_Name, "r")
   except IOError, Message:
       print "File %s could not be opened because\\n%s\\n" \\
             % (File_Name, Message)
       FILE_HANDLE = None
   return FILE_HANDLE

HF = Open_File ("Purdue")
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

def Open_File (File_Name):
   try:
       FILE_HANDLE = open(File_Name, "r")
   except IOError, Message:
       print "File %s could not be opened because \n%s\n" \
             % (File_Name, Message)
       FILE_HANDLE = None
   return FILE_HANDLE

HF = Open_File ("Purdue")

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print """
Trap on an conversion error

N = None
while N == None:
    print "Enter a integer N"
    print "  0 <= N <= 6"
    print "N: ",

    N = sys.stdin.readline()
    N = N.strip()

    try:
        N = int(N)
    except ValueError, Message:
        print
        print "ERROR: Invalid data entered"
        print "   %s" % (Message)
        N = None
    else:
        print
        if (    (N < 0) \
             or (N > 6)):
            print "ERROR: Invalid Selection %d" % (N)
            N = None
         else:
            print "Value entered was ", N
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

N = None
while N == None:
    print "Enter a integer N"
    print "  0 <= N <= 6"
    print "N: ",

    N = sys.stdin.readline()
    N = N.strip()

    try:
        N = int(N)
    except ValueError, Message:
        print
        print "ERROR: Invalid data entered"
        print "   %s" % (Message)
        N = None
    else:
        print
        if (    (N < 0) \
             or (N > 6)):
            print "ERROR: Invalid Selection %d" % (N)
            N = None
        else:
            print "Value entered was ", N

sys.exit(0)
