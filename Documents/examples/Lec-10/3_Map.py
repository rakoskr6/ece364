#!/usr/bin/env python

import sys
import os

# These functions take a single value and produce a new value
def square(x):
	return x*x
	
def cube(x):
	return x*x*x
	
def greater_than_6(x):
	return x > 6
	
# This function takes a list of values and applies a function to each element
# Similar to list comprehension [ f(x) for x in sequence ]
def map(func, items):
	new_items = []
	for i in items:
		new_items.append( func(i) )
	
	return new_items
	
# Using map we can apply a function to each element of a list and produce a new list
A = range(1, 11)
sys.stdout.write("A = %s\n" % (A, ))

# B is a list where each element is squared
B = map(square, A)
sys.stdout.write("B = %s\n" % (B, ))

# C is a list where each element is cubed
C = map(cube, A)
sys.stdout.write("C = %s\n" % (C, ))

# D is a list of booleans indicating if the value is > 6:
D = map(greater_than_6, A)
sys.stdout.write("D = %s\n" % (D, ))

# E is a list of strings
E = map(str, A)
sys.stdout.write("E = %s\n" % (E, ))


sys.exit(0)