#! /usr/bin/env python

#   $Author: ee364 $
#     $Date: 2001/04/10 17:35:21 $
# $Revision: 1.2 $

import sys
import re
import string

print """
   This program expects you to enter a
simple one line regular expression
   Once entered it promts you for
strings to be used to match the the expression
against starting with the beginning of the expression.
"""

Error_Flag = 1
while Error_Flag != 0:
    print """Enter a regular expression:"""
    print "RE: ",
    
    Reg_Expression = sys.stdin.readline()
    Reg_Expression = string.replace(Reg_Expression, "\n" ,"", 1)
   
    try:
        Reg_Exp = re.compile(Reg_Expression)
    except re.error:
        print "Invalid Expression: ", repr(Reg_Expression)
        print
        Error_Flag = 1
    else:
        Error_Flag = 0
    
print """Enter a regular expression:"""
print "RE: ",
    
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

    Match = re.match(Reg_Expression, Search_String)
    if Match != None:
        print Search_String, "--- OK"
        print
        print "Match.pos:", Match.pos
        print "Match.endpos:", Match.endpos
        print "Match.re:", Match.re
        print "Match.string:", Match.string
    else:
        print Search_String, "--- Invalid"

sys.exit(0)
