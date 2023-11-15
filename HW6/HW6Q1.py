from math import *
import numpy as np
from HelperFunctions import *

def x_func(i):
    return -5 + 1/2 * i

def y_func(x):
    return 2 * sin(x) + cos(3*x)

def main(): 
    iterations = 20
    x = [0] * iterations
    y = [0] * iterations
    for iteration in range(iterations):
        x[iteration] = x_func(iteration)
        y[iteration] = y_func(x[iteration])
    
    polynomial = calcNewtonPolynomial(x, y, iterations)
    printPolynomial(polynomial)



if __name__=="__main__": 
    main() 