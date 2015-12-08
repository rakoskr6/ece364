#! /usr/bin/env python

#   $Author: ee364 $
#     $Date: 2001/03/09 14:42:18 $
# $Revision: 1.1 $

import sys

print """
This program looks at 
simple regular expression
"""

print """
Lets examine how to use 
re.search(pattern, string [, flags])

import re

Text_List = ["This was a Big Deal",
             "Who Cares about it!",
             "Today is a good day",
             "EE 364 is real neat",
             "My TA is a good guy"]

Pattern = " is "

print "Searcing for (space)is(space)"

for I in range(len(Text_List)):
    String = Text_List[I]
    print repr (String), ": ",
    print "Search for ", repr (Pattern), "was",
    if re.search(Pattern, String):
        print "successful"
    else:
        print "not successful"
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

import re

Text_List = ["This was a Big Deal",
             "Who Cares about it!",
             "Today is a good day",
             "EE 364 is real neat",
             "My TA is a good guy"]

Pattern = " is "
print "Searcing for (space)is(space)"

for I in range(len(Text_List)):
    String = Text_List[I]
    print repr (String), ": ",
    print "Search for ", repr (Pattern), "was",
    if re.search(Pattern, String):
        print "successful"
    else:
        print "not successful"

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------


print """
Lets examine how to use 
re.search(pattern, string [, flags])

Text_List = ["12345 67890",
             "1 1 1 1 1 1",
             "2 1 1 1 2 3",
             "22 11 22 11",
             "111 333 444",
             "222 111 333",
             "11 22 33 44"]

Pattern = " 1{2} "

print "Searching for a space followed"
print "by at exactly two 1's and a space"

for I in range(len(Text_List)):
    String = Text_List[I]
    print repr (String), ": ",
    print "Search for ", repr (Pattern), "was",
    if re.search(Pattern, String):
        print "successful"
    else:
        print "not successful"
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

Text_List = ["12345 67890",
             "1 1 1 1 1 1",
             "2 1 1 1 2 3",
             "22 11 22 11",
             "111 333 444",
             "222 111 333",
             "11 22 33 44"]

Pattern = " 1{2} "

print "Searching for a space followed"
print "by exactly two 1's and a space"

for I in range(len(Text_List)):
    String = Text_List[I]
    print repr (String), ": ",
    print "Search for ", repr (Pattern), "was",
    if re.search(Pattern, String):
        print "successful"
    else:
        print "not successful"

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print """
Lets examine how to use 
re.search(pattern, string [, flags])

Text_List = ["12345 67890",
             "1 1 1 1 1 1",
             "2 1 1 1 2 3",
             "22 11 22 11",
             "111 333 444",
             "222 111 333",
             "11 22 33 44"]

Pattern = " 1{1,2} "

print "Searching for a space followed by"
print "at least one but no more than two 1's"
print "followed by a space"

for I in range(len(Text_List)):
    String = Text_List[I]
    print repr (String), ": ",
    print "Search for ", repr (Pattern), "was",
    if re.search(Pattern, String):
        print "successful"
    else:
        print "not successful"
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

Text_List = ["12345 67890",
             "1 1 1 1 1 1",
             "2 1 1 1 2 3",
             "22 11 22 11",
             "111 333 444",
             "222 111 333",
             "11 22 33 44"]

Pattern = " 1{1,2} "

print "Searching for a space followed by"
print "at least one but no more than two 1's"
print "followed by a space"

for I in range(len(Text_List)):
    String = Text_List[I]
    print repr (String), ": ",
    print "Search for ", repr (Pattern), "was",
    if re.search(Pattern, String):
        print "successful"
    else:
        print "not successful"

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------


print """
Lets examine how to use 
re.search(pattern, string [, flags])

Text_List = ["12345 67890",
             "1 1 1 1 1 1",
             "2 1 1 1 2 3",
             "22 11 22 11",
             "111 333 444",
             "222 111 333",
             "11 22 33 44"]

Pattern = " 1{2,} "

print "Searching for a space followed by"
print "two or more 1s and a space"

for I in range(len(Text_List)):
    String = Text_List[I]
    print repr (String), ": ",
    print "Search for ", repr (Pattern), "was",
    if re.search(Pattern, String):
        print "successful"
    else:
        print "not successful"
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

Text_List = ["12345 67890",
             "1 1 1 1 1 1",
             "2 1 1 1 2 3",
             "22 11 22 11",
             "111 333 444",
             "222 111 333",
             "11 22 33 44"]

Pattern = " 1{2,} "

print "Searching for a space followed by"
print "two or more 1s and a space"

for I in range(len(Text_List)):
    String = Text_List[I]
    print repr (String), ": ",
    print "Search for ", repr (Pattern), "was",
    if re.search(Pattern, String):
        print "successful"
    else:
        print "not successful"

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------


