#! /usr/bin/env python

#   $Author: ee364 $
#     $Date: 2001/09/21 16:03:14 $
# $Revision: 1.2 $

import sys

print """
This program looks at exception
to help build a simple menu
"""

print """

Items = ("Exit", "EE 364 needs more tests", \\
        "EE 364 needs homework", "EE 364 needs quizzes")
Reply = None
while Reply == None:
    print
    for I in range(0, len(Items)):
        print "%2d: %s" % (I+1, Items[I])
    print "Your Selection: ",

    Reply = sys.stdin.readline()
    Reply = Reply.strip()
    try:
        Reply = int(Reply)
    except ValueError, Message:
        print
        print "ERROR: Invalid data entered"
        print "   %s" % (Message)
        Reply = None
    else:
        print
        if (    (Reply < 0) \
             or (Reply > len(Items)-1)):
            print "ERROR: Invalid Selection %d" % (Reply)
            Reply = None
        elif Items[Reply-1] == "Exit":
            pass
        elif Items[Reply-1] == "EE 364 needs more tests":
            print "How about 3 more?"
            Reply = None
        elif Items[Reply-1] == "EE 364 needs homework":
            print "Ok I'll tell the TAs?"
            Reply = None
        elif Items[Reply-1] == "EE 364 needs quizzes":
            print "Really are you sure?"
            Reply = None
        else:
            Reply = None
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

Items = ("Exit", "EE 364 needs more tests", \
        "EE 364 needs homework", "EE 364 needs quizzes")
Reply = None
while Reply == None:
    print
    for I in range(0, len(Items)):
        print "%2d: %s" % (I+1, Items[I])
    print "Your Selection: ",

    Reply = sys.stdin.readline()
    Reply = Reply.strip()
    try:
        Reply = int(Reply)
    except ValueError, Message:
        print
        print "ERROR: Invalid data entered"
        print "   %s" % (Message)
        Reply = None
    else:
        print
        if (    (Reply < 0) \
             or (Reply > len(Items)- 1)):
            print "ERROR: Invalid Selection %d" % (Reply)
            Reply = None
        elif Items[Reply-1] == "Exit":
            pass
        elif Items[Reply-1] == "EE 364 needs more tests":
            print "How about 3 more?"
            Reply = None
        elif Items[Reply-1] == "EE 364 needs homework":
            print "Ok I'll tell the TAs?"
            Reply = None
        elif Items[Reply-1] == "EE 364 needs quizzes":
            print "Really are you sure?"
            Reply = None
        else:
            Reply = None

sys.exit(0)
