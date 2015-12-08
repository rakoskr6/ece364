#! /usr/bin/env python

#   $Author: ee364 $
#     $Date: 2001/03/09 14:42:41 $
# $Revision: 1.1 $

import sys
import re
import string

print """
   This program expects you to enter a
simple one line regular expression
   The program will fail if an invalid
expession is entered
   Once entered it promts you for
patterns to be used to match the the expression
against starting with the beginning of the expression.
"""

print "Enter a regular expression:"
print "RE: ",
    
Reg_Expression = sys.stdin.readline()
Reg_Expression = string.replace(Reg_Expression, "\n" ,"", 1)

Reg_Exp = re.compile(Reg_Expression)
   
Search_String = ""
while Search_String != "Quit":
    print
    print "Regular Expression:"
    print repr(Reg_Expression)
    print "Enter a string to be matched against"
    print "beginning at the start of the string or"
    print "Quit to exit this program"
    print "Search_String: ",

    Search_String = sys.stdin.readline()
    Search_String = string.replace(Search_String, "\n" ,"", 1)
    print

    if Search_String == "Quit":
        sys.exit(0)
    Match = Reg_Exp.match(Search_String)
    if Match != None:
        print Search_String, "--- OK"
    else:
        print Search_String, "--- Invalid"

sys.exit(0)
