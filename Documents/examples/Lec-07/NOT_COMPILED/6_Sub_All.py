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
   The program the expects you to enter
a replacement string.
   Once both have been entered it promts you for
strings to be used to searched for the pattern 
and replaced with the replacement string
all occurrances will be changed
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
    
    print """Enter a replacement string"""
    print "Replacement String: ",
    
    Replacement_String = sys.stdin.readline()
    Replacement_String= string.replace(Replacement_String, "\n" ,"", 1)
   
Search_String = ""
while Search_String != "Quit":
    print
    print "Regular Expression:"
    print repr(Reg_Expression)
    print "Replacement String:"
    print repr(Replacement_String)
    print "Enter a string to be searched"
    print "replacing all patterns found or"
    print "Quit to exit this program"
    print "Search_String: ",

    Search_String = sys.stdin.readline()
    Search_String = string.replace(Search_String, "\n" ,"", 1)
    print

    if Search_String == "Quit":
        sys.exit(0)

    New_String = re.sub(Reg_Expression,
                        Replacement_String, Search_String)

    print "New_String:", repr(New_String)

sys.exit(0)
