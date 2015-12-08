#!/usr/bin/env python

import sys
import os

# Plain old fibonacci sequence with recursion
def fib(n):
	if n < 2:
		return n
	else:
		return fib(n-1) + fib(n-2)

for i in range(20, 30):
	sys.stdout.write("fib(%d) = %d\n" % (i, fib(i)))
	
# A memoized version of fib
# For large n you should be able to notice the difference in runtime
def fib_memoized(n, table):
	if n in table:
		return table[n]
	elif n < 2:
		table[n] = n
		return n
	else:
		table[n] = fib_memoized(n-1, table) + fib_memoized(n-2, table)
		return table[n]
	

memo_tab = {}
for i in range(20, 30):
	sys.stdout.write("fib_memoized(%d) = %d\n" % (i, fib_memoized(i, memo_tab)))