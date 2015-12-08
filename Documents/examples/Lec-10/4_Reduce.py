#!/usr/bin/env python

import sys
import os

# These functions take two values and produce a single value 
def add(x, y):
	return x + y

def longest(x, y):
	if len(x) > len(y):
		return x
	else:
		return y
		
# This function takes a list of values and reduces it to a single value
# The ident argument represents the base action to occur
def reduce(func, items, ident):
	if len(items) == 0:
		raise ValueError("items was emtpy.")
		
	result = func(ident, items[0])
	for i in items[1:]:
		result = func(result, i)
		
	return result
	
A = range(1, 11)
sys.stdout.write("A = %s\n" % (A, ))

# Reduce a list of elements to a sum
# ident is 0 because 0 is the addative identity of a number
B = reduce(add, A, 0)
sys.stdout.write("B = %s\n" % (B, ))

C = ['fool', 'barbaz', 'b', 'bin']
sys.stdout.write("C = %s\n" % (C, ))

# Get the longest string from a list
# ident is empty string because any string that is not empty will be longer than empty string
D = reduce(longest, C, '')
sys.stdout.write("D = %s\n" % (D, ))


sys.exit(0)