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
	max_error = 0
	for i in range(len(x_arr)):
		error = abs(y_arr[i] - calcPolynomialVal(x_arr[i], p_arr))
		if error > max_error:
			max_error = error
	return max_error
        