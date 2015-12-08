#! /usr/bin/env python

import sys

A = { "Derf Elwom" : 50,
      "Sam Jones" : 70,
      "Pete Brown" : 89,
      "Mary Smith" : 95 }

print A

# Accessing elements of a deictionary A[key]
print 'A["Derf Elwom"] contains', A["Derf Elwom"]
print 'A["Sam Jones"] contains', A["Sam Jones"]
print 'A["Pete Brown"] contains', A["Pete Brown"]
print 'A["Mary Smith"] contains', A["Mary Smith"]

# Get a list of keys
print "A.keys():", A.keys()

# Get a list of values
print "A.values():", A.values()

# Get a list of (key, value) pairs
print "A.items():", A.items()

# Checking if a dictionary contains a key 
List = ["Who cares", "Sam Jones"]
for Item in List:
    if Item in A:
        print Item, "is in A"
    else:
        print Item, "is not in A"

# Getting a value with the get() function:
for Item in List:
    print Item, "has the value", A.get(Item)

# Getting a value with the get function() but return a string when not found
for Item in List:
    print Item, "has the value",
    print A.get(Item, "ERROR NOT A VALID KEY")


sys.exit(0)
