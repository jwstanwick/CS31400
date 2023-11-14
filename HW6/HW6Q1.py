from math import *
import numpy as np

def x_func(i):
    return -5 + 1/2 * i

def y_func(x):
    return 2 * sin(x) + cos(3*x)

def RiseRun(x0, x1, y0, y1):
    return (y1 - y0) / (x1 - x0)

def CalcDividedDifferenceTable(x_arr, y_arr, degree):
	table = np.zeros((degree, degree))
	for i in range(degree):
		table[i][0] = y_arr[i]
	for j in range(1, degree):
		for i in range(degree - j):
			table[i][j] = RiseRun(x_arr[i], x_arr[i + j], table[i][j - 1], table[i + 1][j - 1])
	return table
	
def printPolynomial(polynomial):
    for i in range(len(polynomial)):
        print("a" + str(i) + ": " + str(polynomial[i]))

def main(): 
    iterations = 20
    x = [0] * iterations
    y = [0] * iterations
    for iteration in range(iterations):
        x[iteration] = x_func(iteration)
        y[iteration] = y_func(x[iteration])
    
    dividedDifference = CalcDividedDifferenceTable(x, y, iterations)
    polynomial = dividedDifference[0]    
    printPolynomial(polynomial)



if __name__=="__main__": 
    main() 