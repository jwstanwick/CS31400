from math import *
import numpy as np
import matplotlib.pyplot as plt

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

def plotPoints(x_arr, y_arr, title, x_label, y_label):
	plt.plot(x_arr, y_arr)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.title(title)
	plt.show()

# This code is terrible. And makes me sad. 
# I promise I originally tried to not brute force it.
# But I have an exam tomorrow and I don't have time to make it better. Sorry prof!
def invert3x3(A):
	a, b, c, d, e, f, g, h, i = A[0][0], A[0][1], A[0][2], A[1][0], A[1][1], A[1][2], A[2][0], A[2][1], A[2][2]
	det = a*e*i - a*f*h - b*d*i + b*f*g + c*d*h - c*e*g
	return [[(e*i - f*h)/det, -(b*i - c*h)/det, (b*f - c*e)/det],
			[-(d*i - f*g)/det, (a*i - c*g)/det, -(a*f - c*d)/det],
			[(d*h - e*g)/det, -(a*h - b*g)/det, (a*e - b*d)/det]]

# This QR Factors Code was created with help from:
# - The Berkeley Numerical Methods online textbook - https://pythonnumericalmethods.berkeley.edu/notebooks/chapter15.03-The-QR-Method.html
# - https://johnwlambert.github.io/least-squares/
# - Extra help from ChatGPT
def generateQRFactors(A):
	n, m = len(A), len(A[0])
	Q = [[0]*m for i in range(n)]
	R = [[0]*m for i in range(m)]

	for j in range(m):
		for i in range(n):
			Q[i][j] = A[i][j]
		for k in range(j):
			R[k][j] = sum(Q[i][j] * Q[i][k] for i in range(n))
			for i in range(n):
				Q[i][j] -= R[k][j] * Q[i][k]
		R[j][j] = sqrt(sum(Q[i][j]**2 for i in range(n)))
		for i in range(n):
			Q[i][j] /= R[j][j]
	return Q, R

# Solving a back substitution problem for an upper triangular matrix U and a vector b
def backSubstitution(U, b):
	n = len(U)
	x = np.zeros(n)
	for i in range(n - 1, -1, -1):
		x[i] = b[i]
		for j in range(i + 1, n):
			x[i] -= U[i][j] * x[j]
		x[i] /= U[i][i]
	return x