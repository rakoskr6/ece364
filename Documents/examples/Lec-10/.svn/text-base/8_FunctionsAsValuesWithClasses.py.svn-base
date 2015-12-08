#!/usr/bin/env python

import sys
import os

# This example shows that even member functions can be treated like values

def regular_function(x, y):
	return x + y

class value:
	def __init__(self, value):
		self.value = value
	
	def add(self, other):
		return value(self.value + other.value)
		
	def __add__(self, other):
		return self.add(other)
	
	def __str__(self):
		return "~%s~" % (self.value)
		
A = value(10)
B = value(11)
sys.stdout.write("A = %s\nB = %s\n\n" % (A, B))

# Notice that A.add is called a "bound" method
# In this case the object A is bound to the first argument already
# A.add can be passed to other functions just like a regular function
my_function = A.add
sys.stdout.write("regular_function = %s\n" % (regular_function,))
sys.stdout.write("my_function = %s\n\n" % (my_function, ))

# my_function already has the first argument bound so we only pass the second
C = my_function(B)
sys.stdout.write("C = my_function(B) = %s\n" % (C,))

D = regular_function(A, B)
sys.stdout.write("D = regular_function(A, B) = %s\n" % (D,))
sys.exit(0)