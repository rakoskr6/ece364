#! /usr/bin/env python

import os, sys

def factorial_recursive(n=0):

    if n > 30:
        sys.stderr.write("factorial_recursive: n = %d is too large!\n" % (n,))
        sys.exit(1)
    
    if n == 0 or n == 1 or n < 0:
        return 1
    else:
        return factorial_recursive(n-1) * n

def factorial(n=0):
    
    if n < 0:
        return 1
        
    for i in range(1, n):
        n = n * i

    return n

def Func(A=30, B=3):
  Sum = A + B
  Dif = A - B
  Mul = A * B
  Div = A / B
  return (Sum, Dif, Mul, Div)

n = int(raw_input("n = ").strip())
print factorial_recursive(n), factorial(n)

# Just a standard function call
(MySum, MyDif, MyMul, MyDiv) = Func(n, 7) 
print MySum, MyDif, MyMul, MyDiv

# Last argument of Func is not provided, will use default argument value
(MySum, MyDif, MyMul, MyDiv) = Func(n) 
print MySum, MyDif, MyMul, MyDiv

# No arguments provided to Func, will use default argument values
(MySum, MyDif, MyMul, MyDiv) = Func() 
print MySum, MyDif, MyMul, MyDiv


sys.exit(0)

