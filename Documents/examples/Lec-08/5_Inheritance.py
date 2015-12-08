#! /usr/bin/env python

import os, sys

class Polygon:
    def __init__(self):
        pass

    def area(self):
        # Member function: compute the area of the polygon
        pass

    def perimeter(self):
        # Member function: compute the perimeter of the polygon
        pass

    def name(self):
        return "Polygon"

    def __str__(self):
        # Member function (special): returns the string representation of the polygon
        return "%s area=%f, perimeter=%f" % (self.name(), self.area(), self.perimeter())

class Square(Polygon):
    def __init__(self, width):
        Polygon.__init__(self)
        self.width = width
    
    def area(self):
        return self.width * self.width

    def perimeter(self):
        return 4 * self.width

    def name(self):
        return "Square"

class Rectangle(Polygon):
    def __init__(self, width, length):
        Polygon.__init__(self)
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2*self.width + 2*self.length

    def name(self):
        return "Rectangle"

class Pentagon(Polygon):
    def __init__(self, side):
        Polygon.__init__(self)
        self.side = side

    def area(self):
        return 1.720477401 * self.side * self.side

    def perimeter(self):
        return 5 * self.side

    def name(self):
        return "Pentagon"

# Initialize some shapes
s = Square(10.0)
r = Rectangle(10.0, 3.75)
p = Pentagon(7.50)

print "Square: %s" % (s,)
print "Rectangle: %s" % (r,)
print "Pentagon: %s" % (p,)
print

# Each Shape implements the same set of functions so we can treat them all the same
for shape in [s, r, p]:
    print "%s has a perimeter of %f" % (shape.name(), shape.perimeter())

sys.exit(0)
