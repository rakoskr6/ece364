#! /usr/bin/env python

#   $Author: ee364 $
#     $Date: 2001/03/09 14:42:18 $
# $Revision: 1.1 $

import sys

print """
This program looks at 
advanced regular expressions
"""

print """
Lets use re.findall(pattern, string)

import re

Text_List = ["This was a Big Deal",
             "Who Cares about it!",
             "Today is a good day",
             "EE 364 is real neat",
             "My TA is a good guy"]

Pattern = "(?i)e"  

print "Extract all e's case insensitive"

for I in range(len(Text_List)):
    String = Text_List[I]
    print repr (String), ": ",
    Extracted = re.findall(Pattern, String)
    print "Extracted:", Extracted
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

Pattern = "(?i)e"  

print "Extract all e's case insensitive"

for I in range(len(Text_List)):
    String = Text_List[I]
    print repr (String), ": ",
    Extracted = re.findall(Pattern, String)
    print "Extracted:", Extracted

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print """
Lets use groups to help extract information

This will be a greedy extraction

String = "This is not his house!"

Pattern = "(.*)(is)(.*)"

Extracted = re.findall(Pattern, String)

print "Extracted:", Extracted
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

String = "This is not his house!"

Pattern = "(.*)(is)(.*)"

Extracted = re.findall(Pattern, String)

print "Extracted:", Extracted

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print """
Lets use groups to help extract information

This will be a non greedy extraction

String = "This is not his house!"

Pattern = "(.*?)(is)(.*)"

Extracted = re.findall(Pattern, String)

print "Extracted:", Extracted
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

String = "This is not his house!"

Pattern = "(.*?)(is)(.*?)"

Extracted = re.findall(Pattern, String)

print "Extracted:", Extracted

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------


print """
Lets use Named groups to help extract information

This will be a non greedy extraction

String = "This is not his house!"


Pattern = "(?P<First>.*?)(?P<Second>is)(?P<Third>.*)"

Extracted = re.match(Pattern, String)

print "First:", Extracted.group('First')
print "Second:", Extracted.group('Second')
print "Third:", Extracted.group('Third')
"""

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

String = "This is not his house!"

Pattern = "(?P<First>.*?)(?P<Second>is)(?P<Third>.*)"

Extracted = re.match(Pattern, String)

print "First:", Extracted.group('First')
print "Second:", Extracted.group('Second')
print "Third:", Extracted.group('Third')

sys.exit(0)
