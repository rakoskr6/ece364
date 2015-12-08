#!/usr/bin/env python


import sys
import os

# A class that represents a function that compute fibbonacci numbers
class fibonacci:
	def __init__(self):
		self.table = {}
		
	def fib(self, n):
		# Compute the nth fibonacci number
		if n in self.table:
			return self.table[n]
		elif n < 2:
			self.table[n] = n
			return n
		else:
			# Call r
			self.table[n] = self.fib(n-1) + self.fib(n-2)
			return self.table[n]	

	def get_sequence(self, n):
		# Returns a tuple representing the fibonacci sequence
		return tuple([ self.fib(x) for x in range(1,n+1) ])
	
	def __call__(self, n):
		# Overloads the call () operator
		return self.fib(n)
		
	def __str__(self):
		# Overloads the str() function
		return "<fibonacci: %s>" % (self.table)
	
# We can instantiate an object and call it like a function
memo_fib = fibonacci()
for i in range(20, 30):
	sys.stdout.write("memo_fib(%d) = %d\n" % (i, memo_fib(i)))
	
# Printing out reveals the state
sys.stdout.write("\nmemo_fib = %s\n\n" % (memo_fib,))

# memo_fib is just an object se we can also call member functions
sys.stdout.write("Fibonacci Sequence:\n%s\n\n" % (memo_fib.get_sequence(40),))

# Printing out reveals the state (updated)
sys.stdout.write("\nmemo_fib = %s\n\n" % (memo_fib,))

sys.exit(0)
