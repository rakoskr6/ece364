#!/usr/bin/env python

import sys
import os

# These are typical Python functions
def Add(x, y):
	return x + y

def Multiply(x, y):
	return x * y

a = 10
b = 20
c = Add(a, b)
sys.stdout.write("Add(%d, %d) = %d\n" % (a, b, c))

d = Multiply(a, b)
sys.stdout.write("Multiply(%d, %d) = %d\n" % (a, b, d))

# What is a function? Its just an object!
sys.stdout.write("\n%s\n%s\n" % (Add, Multiply))

# Notice above that the function name can be treated like a variable.
# In fact functions can be assigned.
func = Add
sys.stdout.write("\nfunc = %s\n" % (func,))

# If a value is a function, it can be called!
e = func(a, b)
sys.stdout.write("func(%d, %d) = %d\n" % (a, b, e))

# Functions can be treated like other variables in python and added to containers
functions = {'+':Add, '*':Multiply}
operations = (Add, Multiply)

g = functions['*'](a, b)
sys.stdout.write("\nfunctions['*'](%d, %d) = %d\n" % (a, b, g))

h = operations[0](a, b)
sys.stdout.write("operations[0](%d, %d) = %d\n" % (a, b, h))

sys.exit(0)
