from math import *
import numpy as np
from HW6Q1 import CalcDividedDifferenceTable, printPolynomial

def Q2a(n):
	def x_func(i):
		return -1 + 1/2 * i
	def y_func(x):
		return sin(x)
	x = [x_func(i) for i in range(n)]
	y = [y_func(x) for x in x]
	dividedDifference = CalcDividedDifferenceTable(x, y, n)
	return dividedDifference[0]

def Q2b(n):
	def x_func(i):
		return cos(pi * i / 4)
	def y_func(x):
		return sin(x)
	x = [x_func(i) for i in range(n)]
	y = [y_func(x) for x in x]
	dividedDifference = CalcDividedDifferenceTable(x, y, n)
	return dividedDifference[0]
    
def Q2ci(i, n):
    def x_func(i, n):
        return -1 + (1 - (-1))/n * i
    x = [x_func(i, n) for i in range(i)]
    #What is the maximum interpolation error E1 (i.e., E1 = maxx∈[−1,1] |f(x) −pn(x)|)?
    

def main(): 
    Q2a_sol = Q2a(5)
    print("Q2a: ")
    printPolynomial(Q2a_sol)
    print("")
    
    Q2b_sol = Q2b(5)
    print("Q2b: ")
    printPolynomial(Q2b_sol)
    print("")
    

if __name__=="__main__":
    main()