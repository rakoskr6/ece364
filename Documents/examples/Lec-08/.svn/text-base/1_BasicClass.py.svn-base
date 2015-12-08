#! /usr/bin/env python

import os, sys

##
## CLASS DEFINITIONS
##

class DataSet:

    def __init__(self, name):        
        # Member variable: Name of the data set
        self.name = str(name)

        # Member variable: set of floating point values in the set
        self.values = []

    def add_item(self, v):
        # Member function: Adds a value to the list of values        
        self.values.append(float(v))

    def get_stats(self):
        # Member function: Returns a tuple with some basic stats
        return (len(self.values), min(self.values), max(self.values), sum(self.values)/len(self.values))

##            
## MAIN PROGRAM
##

# Instantiation: Create an instance of the DataSet class and assign it to the variable DS1
DS1 = DataSet("Set 1")

# Instantiation: Create an instance of the DataSet class and assign it to the variable DS2
DS2 = DataSet("Set 2")

# Observe the print behavior:
# DS1 and DS2 are two distinct objects at different memory locations
print "DS1 is ", DS1
print "DS2 is ", DS2

# Accessing member variables:
print "DS1.values = ", DS1.values

# Calling member functions:
for i in range(1, 10):
    # We invoke the same member function but on different references
    DS1.add_item(0.25 * i)
    DS2.add_item(0.50 * i)

# The member variables of DS1 and DS2 are not shared in this example and contain two distinct lists
print "DS1.values = ", DS1.values
print "DS2.values = ", DS2.values

# Knowing that the values member variable is a list we can modify it directly...
DS1.values.append(DS1.values[0] + DS2.values[0])
DS2.values.append(DS1.values[1] + DS2.values[1])

print "DS1.values = ", DS1.values
print "DS2.values = ", DS2.values


# To finish this example we will print the stats of each data set:
print "%s: %s" % (DS1.name, DS1.get_stats())
print "%s: %s" % (DS2.name, DS2.get_stats())
    

sys.exit(0)
