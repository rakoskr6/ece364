#! /usr/bin/env python

import sys

# String length
String1 = "This is String1!"
print "String1 is %d characters long." % (len(String1),)


# String concatenation
String2 = "Hello"
String3 = "World"
print String2 + " " + String3


# Stripping whitespace
String4 = "     This string has     extra whitespace\n\n"
print String4

# Notice that only the ends of the string have whitespace removed
String5 = String4.lstrip()
String6 = String4.rstrip()
String7 = String4.strip()

# Functions that return values can sometimes be chained together
# Here lstrip() returns a string that we call rstrip() on
String8 = String4.lstrip().rstrip()

print String5
print String6
print String7
print String8

# Strings can be compared and ordered
String9="Foo"
String10="Bar"
String11="Baz"
String12="Foo"

if String9 == String12:
    print "\"%s\" is equal to \"%s\"" % (String9, String12)

if String11 != String12:
    print "\"%s\" is not qual to \"%s\"" % (String11, String12)

if String10 < String11:
    print "\"%s\" comes before \"%s\"" % (String10, String11)

sys.exit(0)
