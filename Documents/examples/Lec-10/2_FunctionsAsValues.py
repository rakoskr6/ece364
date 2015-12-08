#!/usr/bin/env python

import sys
import os

def Add(x, y):
	return x + y

def Multiply(x, y):
	return x * y

def calculate(op, x, y):
	# op is very much like a function pointer from C
	sys.stdout.write("Calling %s with arguments %.3f and %.3f.\n" % (op, x, y))
	return op(x, y)

a = 5.89
b = 6.78

# Recall that functions can be passed around
c = calculate(Add, a, b)
sys.stdout.write("calculate(Add, %.3f, %.3f) = %.3f\n\n" % (a, b, c))

d = calculate(Multiply, a, b)
sys.stdout.write("calculate(Multiply, %.3f, %.3f) = %.3f\n\n" % (a, b, d))

sys.exit(0)
