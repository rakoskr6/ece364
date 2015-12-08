#! /usr/bin/env python

#   $Author: ee364 $
#     $Date: 2001/03/09 14:42:18 $
# $Revision: 1.1 $

import sys
import re
import string
#import pcre


print '''
Search_String = """
100 50.50 70.00
2 2.3 .4 00.00 12a.b34
-2 -2.0 -.89 +3 +12.34 +.987
"""

Reg_Expression = """
(?x)
(?# signed and unsigned integers)
[+-]?\d+
"""

Replacement_String = "*"

print "Search_String:", Search_String
print "Reg_Expression:", Reg_Expression
print "Replacement_String:\\n", Replacement_String

New_String = re.subn(Reg_Expression, Replacement_String, Search_String)

print "New_String:\\n", New_String[0]
print "Number of changes:", New_String[1]
'''

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

Search_String = """
100 50.50 70.00
2 2.3 .4 00.00 12a.b34
-2 -2.0 -.89 +3 +12.34 +.987
"""

Reg_Expression = """
(?x)
(?# signed and unsigned integers)
[+-]?\d+
"""

Replacement_String = "*"

print "Search_String:", Search_String
print "Reg_Expression:", Reg_Expression
print "Replacement_String:\n", Replacement_String

New_String = re.subn(Reg_Expression, Replacement_String, Search_String)

print "New_String:\n", New_String[0]
print "Number of changes:", New_String[1]

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print '''
Search_String = """
100 50.50 70.00
2 2.3 .4 00.00 12a.b34
-2 -2.0 -.89 +3 +12.34 +.987

Selection order is not correct
"""

Reg_Expression = """
(?x)
(?# signed and unsigned decimal numbers)
[+-]?
(   [0-9]+[.]         (?# 1 or more digits followed by .) 
  | [.][0-9]+         (?# . followed by 1 or more digits)
  | [0-9]+[.][0-9]+   (?# digits . digits)
)
"""

Replacement_String = "*"

print "Search_String:", Search_String
print "Reg_Expression:", Reg_Expression
print "Replacement_String:\\n", Replacement_String

New_String = re.subn(Reg_Expression, Replacement_String, Search_String)

print "New_String:\\n", New_String[0]
print "Number of changes:", New_String[1]
'''

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

Search_String = """
100 50.50 70.00
2 2.3 .4 00.00 12a.b34
-2 -2.0 -.89 +3 +12.34 +.987
"""

Reg_Expression = """
(?x)
(?# signed and unsigned decimal numbers)
[+-]?
(   [0-9]+[.]         (?# 1 or more digits followed by .) 
  | [.][0-9]+         (?# . followed by 1 or more digits)
  | [0-9]+[.][0-9]+   (?# digits . digits)
)
"""

Replacement_String = "*"

print "Search_String:", Search_String
print "Reg_Expression:", Reg_Expression
print "Replacement_String:\n", Replacement_String

New_String = re.subn(Reg_Expression, Replacement_String, Search_String)

print "New_String:\n", New_String[0]
print "Number of changes:", New_String[1]

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print '''
Search_String = """
100 50.50 70.00
2 2.3 .4 00.00 12a.b34
-2 -2.0 -.89 +3 +12.34 +.987

A little better
"""

Reg_Expression = """
(?x)
(?# signed and unsigned decimal numbers)
[+-]?
(   [0-9]+[.][0-9]+   (?# digits . digits)
  | [0-9]+[.]         (?# 1 or more digits followed by .) 
  | [.][0-9]+         (?# . followed by 1 or more digits)
)
"""

Replacement_String = "*"

print "Search_String:", Search_String
print "Reg_Expression:", Reg_Expression
print "Replacement_String:\\n", Replacement_String

New_String = re.subn(Reg_Expression, Replacement_String, Search_String)

print "New_String:\\n", New_String[0]
print "Number of changes:", New_String[1]
'''

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

Search_String = """
100 50.50 70.00
2 2.3 .4 00.00 12a.b34
-2 -2.0 -.89 +3 +12.34 +.987
"""

Reg_Expression = """
(?x)
(?# signed and unsigned decimal numbers)
[+-]?
(   [0-9]+[.][0-9]+   (?# digits . digits)
  | [0-9]+[.]         (?# 1 or more digits followed by .) 
  | [.][0-9]+         (?# . followed by 1 or more digits)
)
"""

Replacement_String = "*"

print "Search_String:", Search_String
print "Reg_Expression:", Reg_Expression
print "Replacement_String:\n", Replacement_String

New_String = re.subn(Reg_Expression, Replacement_String, Search_String)

print "New_String:\n", New_String[0]
print "Number of changes:", New_String[1]

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print '''
Search_String = """
100 50.50 70.00
2 2.3 .4 00.00 12a.b34
-2 -2.0 -.89 +3 +12.34 +.987

Incorrectly Checking for white space
"""

Reg_Expression = """
(?x)
(?# signed and unsigned decimal numbers)
(\s)*                 (?# 0 or more white space)
[+-]?                 (?# 0 or 1 + - sign)
(   [0-9]+[.][0-9]+   (?# digits . digits)
  | [0-9]+[.]         (?# 1 or more digits followed by .) 
  | [.][0-9]+)        (?# . followed by 1 or more digits)
(\s+|\Z)              (?# white space or end of string)
"""

Replacement_String = "*"

print "Search_String:", Search_String
print "Reg_Expression:", Reg_Expression
print "Replacement_String:\\n", Replacement_String

New_String = re.subn(Reg_Expression, Replacement_String, Search_String)

print "New_String:\\n", New_String[0]
print "Number of changes:", New_String[1]
'''

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

Search_String = """
100 50.50 70.00
2 2.3 .4 00.00 12a.b34
-2 -2.0 -.89 +3 +12.34 +.987
"""

Reg_Expression = """
(?x)
(?# signed and unsigned decimal numbers)
(\s)*                 (?# 0 or more white space)
[+-]?                 (?# 0 or 1 + - sign)
(   [0-9]+[.][0-9]+   (?# digits . digits)
  | [0-9]+[.])        (?# 1 or more digits followed by .) 
  | [.][0-9]+         (?# . followed by 1 or more digits)
(\s+|\Z)              (?# white space or end of string)
"""

Replacement_String = "*"

print "Search_String:", Search_String
print "Reg_Expression:", Reg_Expression
print "Replacement_String:\n", Replacement_String

New_String = re.subn(Reg_Expression, Replacement_String, Search_String)

print "New_String:\n", New_String[0]
print "Number of changes:", New_String[1]

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print '''
Search_String = """
100 50.50 70.00
2 2.3 .4 00.00 12a.b34
-2 -2.0 -.89 +3 +12.34 +.987

Correct check for white space
"""

Reg_Expression = """
(?x)
(?# signed and unsigned decimal numbers)
(\s*)                      (?# 0 or more white space)
(   [+-]?[0-9]+[.][0-9]+   (?# digits . digits)
  | [+-]?[.][0-9]+         (?# . followed by 1 or more digits)
  | [+-]?[0-9]+[.])        (?# 1 or more digits followed by .) 
(\s+|\Z)                   (?# white space or end of string)
"""

Replacement_String = "\\1*\\3"   # double \\ are needed

print "Search_String:", Search_String
print "Reg_Expression:", Reg_Expression
print "Replacement_String:\\n", Replacement_String

New_String = re.subn(Reg_Expression, Replacement_String, Search_String)

print "New_String:\\n", New_String[0]
print "Number of changes:", New_String[1]
'''

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

Search_String = """
100 50.50 70.00
2 2.3 .4 00.00 12a.b34
-2 -2.0 -.89 +3 +12.34 +.987
"""

Reg_Expression = """
(?x)
(?# signed and unsigned decimal numbers)
(\s*)                      (?# 0 or more white space)
(   [+-]?[0-9]+[.][0-9]+   (?# digits . digits)
  | [+-]?[.][0-9]+         (?# . followed by 1 or more digits)
  | [+-]?[0-9]+[.])        (?# 1 or more digits followed by .) 
(\s+|\Z)                   (?# white space or end of string)
"""

Replacement_String = "\\1*\\3"   # double \\ are needed

print "Search_String:", Search_String
print "Reg_Expression:", Reg_Expression
print "Replacement_String:\n", Replacement_String

New_String = re.subn(Reg_Expression, Replacement_String, Search_String)

print "New_String:\n", New_String[0]
print "Number of changes:", New_String[1]

print "\nPress Enter to continue: ",
Pause = sys.stdin.readline ()
print

# ------------------------------------------------

print '''
Search_String = """
100 50.50 70.00
2 2.3 .4 00.00 12a.b34
-2 -2.0 -.89 +3 +12.34 +.987
"""

Reg_Expression = """
(?x)
(?# signed and unsigned decimal numbers)
(   [+-]?[0-9]+[.][0-9]+   (?# digits . digits)
  | [+-]?[.][0-9]+         (?# . followed by 1 or more digits)
  | [+-]?[0-9]+[.])        (?# 1 or more digits followed by .) 
"""

print "Search_String:", Search_String
print "Reg_Expression:", Reg_Expression

Data = re.findall(Reg_Expression, Search_String)

print "Data Extracted\\n:", Data
'''

print "\nPress Enter for output: ",
Pause = sys.stdin.readline ()
print

# ************************************************

Search_String = """
100 50.50 70.00
2 2.3 .4 00.00 12a.b34
-2 -2.0 -.89 +3 +12.34 +.987
"""

Reg_Expression = """
(?x)
(?# signed and unsigned decimal numbers)
(   [+-]?[0-9]+[.][0-9]+   (?# digits . digits)
  | [+-]?[.][0-9]+         (?# . followed by 1 or more digits)
  | [+-]?[0-9]+[.])        (?# 1 or more digits followed by .) 
"""

print "Search_String:", Search_String
print "Reg_Expression:", Reg_Expression

Data = re.findall(Reg_Expression, Search_String)

print "Data Extracted\n:", Data


sys.exit(0)
