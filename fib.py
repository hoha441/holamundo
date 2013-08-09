#!/usr/bin/env python
def fib (n):
   """Imprime una serie Fibonacci hasta n"""
   a,b=0,1
   while b<n:
	print b,
	a,b = b,a+b

fib(3)
