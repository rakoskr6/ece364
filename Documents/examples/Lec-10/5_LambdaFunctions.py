#!/usr/bin/env python

import sys
import os

def print_y(y):
	sys.stdout.write("print_y: " + y)

# Lambda expression evaluate to a function
# print_x is assigned an unmaed function that prints the value x to stdout
print_x = lambda x: sys.stdout.write("print_x: " + x)

sys.stdout.write("print_y = %s\n" % (print_y,))
sys.stdout.write("print_x = %s\n" % (print_x,))

# print_x is a function value and can be called
print_y("ECE 364 is a blast!\n")
print_x("ECE 364 is a 1 credit hour course.\n\n")

# Perhaps a more interesting use of lambda is a ability to provide it as
# an argument to another function
def calc(op, x, y):
	return op(x, y)
	
a = 10
b = 20

c = calc(lambda z, w: z+w, a, b)
sys.stdout.write("c = %d\n\n" % (c,))

# Lambda is helpful when you want to pass a function withot formally defining one
# Consider the sorted() function that produces a sorted set of things
A = [10, 99, 56, -4, 53, 7]
sys.stdout.write("A = %s\n" % (A,))

B = sorted(A)
sys.stdout.write("B = %s\n" % (B,))

# What if what is beign sorted is not a list of plain value but more complex objects
# Most of the time we need to specifiy what value is used for the key when comparing elements
# In our example the 2nd element of the items of the list will be used
C = [(88.2, "Goldfarb"), (99.3, "Lamers"), (45.3, "Derf Elwom")]
sys.stdout.write("C = %s\n" % (C,))

def get_key(elem):
	# 2nd element is the "key"
	return elem[1]
	
# If the key argument is supplied the name of a function
# The internal sorting algorithm will call the function to get the key value
D = sorted(C, key=get_key)
sys.stdout.write("D = %s\n" % (D,))

# Rather than write a formal function we can use a lambda expression
E = sorted(C, key=lambda e: e[1])
sys.stdout.write("E = %s\n" % (E,))

sys.exit(0)

