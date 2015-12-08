#! /usr/bin/env python

# Reads in a set of numbers from stdin and builds a list of points
# A point will be formed by a tuple e.g. (x,y)

import sys

points=[]

for line in sys.stdin:
    line = line.strip()

    # Whitespace separated
    coords = line.split() 

    if len(coords) != 2:
        sys.stderr.write("Invalid point! Only 2-d points are accepted.")
        sys.exit(1)

    # Make a new tuple (x,y):
    point = (float(coords[0]), float(coords[1]))
    
    # Add it to the list of points:
    points.append(point)
    
print "The points are:"
print points

sys.exit(0)
