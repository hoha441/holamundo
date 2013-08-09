#!/usr/bin/env python
def fib (n):
   """Imprime una serie Fibonacci hasta n"""
   a,b=0,1
   while b<n:
	print b,
	a,b = b,a+b
'''import fib te ejecuta'''

def fib2(n):
    result=[]
    a,b = 0,1
    while b<n:
      result.append(b)
      a,b = b,a+b
    return result
