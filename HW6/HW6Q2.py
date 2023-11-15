from math import *
import numpy as np
import matplotlib.pyplot as plt
from HelperFunctions import *
from SolutionChecking import _poly_newton_coefficient

def Q2a(n):
	def x_func(i):
		return -1 + 1/2 * i
	def y_func(x):
		return sin(x)
	x = [x_func(i) for i in range(n)]
	y = [y_func(x_val) for x_val in x]
	return calcNewtonPolynomial(x, y, n)

def Q2b(n):
	def x_func(i):
		return cos(pi * i / 4)
	def y_func(x):
		return sin(x)
	x = [x_func(i) for i in range(n)]
	y = [y_func(x_val) for x_val in x]
	return calcNewtonPolynomial(x, y, n)
	
def Q2ci(n):
	def x_func(i, n):
		return -1 + (1 - (-1))/n * i
	def y_func(x):
		return sin(x)
	x = [x_func(i, n) for i in range(n + 1)]
	y = [y_func(x_val) for x_val in x]
 
	p = calcNewtonPolynomial(x, y, n)
	return maxInterpolationError(x, y, p)

def Q2cii(n):
	def x_func(i):
		return cos(pi * i / n)
	def y_func(x):
		return sin(x)
	x = [x_func(i) for i in range(n + 1)]
	y = [y_func(x_val) for x_val in x]
 
	p = calcNewtonPolynomial(x, y, n)
	return maxInterpolationError(x, y, p)

# This function plots the max interpolation error of q2ci for n = 3, 4, 5, 6, 7
def Q2di():
    errorArr = []
    for n in range(3, 8):
        errorArr.append(Q2ci(n))
    
    plt.plot([3, 4, 5, 6, 7], errorArr)
    plt.xlabel("n")
    plt.ylabel("Max Interpolation Error")
    plt.title("Equal Spaced Points Max Interpolation Error vs n")
    plt.show()

# This function plots the max interpolation error of q2cii for n = 3, 4, 5, 6, 7
def Q2dii():
    errorArr = []
    for n in range(3, 8):
        errorArr.append(Q2cii(n))
    
    plt.plot([3, 4, 5, 6, 7], errorArr)
    plt.xlabel("n")
    plt.ylabel("Max Interpolation Error")
    plt.title("Chebyshev Max Interpolation Error vs N")
    plt.show()

def main(): 
	Q2a_sol = Q2a(5)
	print("Q2a: ")
	printPolynomial(Q2a_sol)
	print("")
	
	Q2b_sol = Q2b(5)
	print("Q2b: ")
	printPolynomial(Q2b_sol)
	print("")
	
	Q2ci_sol = Q2ci(5)
	print(f"Q2ci Max Interpolation Error: {round(Q2ci_sol, 6)}")
 
	Q2cii_sol = Q2cii(5)
	print(f"Q2cii Max Interpolation Error: {round(Q2cii_sol, 6)}")
 
	Q2di()
	Q2dii()
	

if __name__=="__main__":
	main()