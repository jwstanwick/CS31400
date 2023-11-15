from math import *
import numpy as np

def riseRun(x0, x1, y0, y1):
    return (y1 - y0) / (x1 - x0)

def calcNewtonPolynomial(x_arr, y_arr, degree):
	table = np.zeros((degree, degree))
	for i in range(degree):
		table[i][0] = y_arr[i]
	for j in range(1, degree):
		for i in range(degree - j):
			table[i][j] = riseRun(x_arr[i], x_arr[i + j], table[i][j - 1], table[i + 1][j - 1])
	return table[0]
	
def printPolynomial(polynomial):
    for i in range(len(polynomial)):
        print(f"a{i}: {round(polynomial[i], 6)}")
        
def calcPolynomialVal(x, polynomial):
	val = 0
	for i in range(len(polynomial)):
		val += polynomial[i] * x ** i
	return val

# Find the maximum interpolation error for f(x) - p(x)
def maxInterpolationError(x_arr, y_arr, p_arr):
	degree = len(x_arr) - 1   
	max_error = -1
	max_derivative_val = 1
 
	for cur_x in x_arr:
		product_term = 1
		for x in x_arr:
			if cur_x == x:
				continue
			else:
				product_term = product_term * (cur_x - x)
		error = max_derivative_val / factorial(degree + 1) * product_term
		if abs(error) > max_error:
			max_error = abs(error)
	return max_error
        