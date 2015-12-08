#! /usr/bin/env python

# The sys module contains many important and commonly used functions
import sys

print "There are %d command line arguments passed to this script." % (len(sys.argv),)

print "The command line arguments list is: ", sys.argv

# A simple if statement to check the number of arguments 
if len(sys.argv) == 1:
    print "Not enough arguments!"
    sys.exit(1)

if len(sys.argv) % 2 == 0:
    print "There is an even number of arguments."
else:
    print "There is an odd number of arguments."


print "The arguments again:"

# A for loop
for arg in sys.argv:
    print arg


# Always exit your script with the appropriate exit code
sys.exit(0)
