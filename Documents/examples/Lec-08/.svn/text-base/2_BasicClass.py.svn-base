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

datasets = []

try:
    fp = open("2_BasicClass.input", "r")
except:
    sys.stderr.write("Could not open input file: 2_BasicClass.input")
    sys.exit(1)



for line in fp:
    # Each line in the file represents a dataset
    line = line.split(',')

    # Construct a new dataset
    ds = DataSet(line[0])

    # Add values to it
    for v in line[1:]:
        ds.add_item(float(v))

    # Add the new data set to the collection of datasets
    datasets.append(ds)
    
fp.close()

# The list datasets contains instances of DataSet objects
print datasets

# We can loop over each data set in the list
for ds in datasets:
    print "%s:  average = %3.3f" % (ds.name, ds.get_stats()[3])

sys.exit(0)
