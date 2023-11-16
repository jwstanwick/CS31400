import numpy as np
from math import *
from HelperFunctions import *

x_arr = np.array([-5, -4.6552, -4.3103, -3.9655, -3.6207, 
         -3.2759, -2.931, -2.5862, -2.2414, -1.8966, 
         -1.5517, -1.2069, -0.86207, -0.51724, -0.17241, 
         0.17241, 0.51724, 0.86207, 1.2069, 1.5517, 1.8966, 
         2.2414, 2.5862, 2.931, 3.2759, 3.6207, 3.9655, 4.3103, 
         4.6552, 5])

y_arr = np.array([25.198, 22.354, 11.286, -5.3643, -9.9406, 5.5574, 20.364, 
         10.826, 12.018, 18.742, -4.5468, -6.2935, 11.038, -6.9372, 
         22.685, 10.281, -4.0523, -0.26773,10.089, 13.64, 20.074,
         13.906, 2.7136, 16.384, 2.9209, 27.113, 30.377, 29.667,
         22.724, 48.731])

# Implement a program to derive the least squares quadratic polynomial by solving the normal equations. State the limitation of this approach.

def Q3a(x_arr, y_arr):
    sum_x4 = np.sum(x_arr ** 4)
    sum_x3 = np.sum(x_arr ** 3)
    sum_x2 = np.sum(x_arr ** 2)
    sum_x = np.sum(x_arr)
    sum_x2y = np.sum(x_arr ** 2 * y_arr)
    sum_xy = np.sum(x_arr * y_arr)
    sum_y = np.sum(y_arr)
    
    A = np.array([
        [sum_x4, sum_x3, sum_x2], 
        [sum_x3, sum_x2, sum_x], 
        [sum_x2, sum_x, len(x_arr)]
    ])
    
    b = np.array([sum_x2y, sum_xy, sum_y]) 
    
    # Whoops, not allowed to use .linalg.solve!
    # polynomial = np.linalg.solve(A, b)
    polynomial = invert3x3(A.T @ A) @ A.T @ b
    
    return polynomial

# Implement a program to derive the least square quadratic polynomial using QR factorization that finds the orthogonal projection of b onto the column space of A.
def Q3b(x_arr, y_arr):
    sum_x4 = np.sum(x_arr ** 4)
    sum_x3 = np.sum(x_arr ** 3)
    sum_x2 = np.sum(x_arr ** 2)
    sum_x = np.sum(x_arr)
    sum_x2y = np.sum(x_arr ** 2 * y_arr)
    sum_xy = np.sum(x_arr * y_arr)
    sum_y = np.sum(y_arr)
    
    A = np.array([
        [sum_x4, sum_x3, sum_x2], 
        [sum_x3, sum_x2, sum_x], 
        [sum_x2, sum_x, len(x_arr)]
    ])
    b = np.array([sum_x2y, sum_xy, sum_y]) 
    
    Q, R = generateQRFactors(A)
    Q = np.array(Q)
    R = np.array(R)
    
    QTB = Q.T @ b
    
    polynomial = backSubstitution(R, QTB)
    return polynomial

def main():
    PLOT = True
    
    Q3a_sol = Q3a(x_arr, y_arr)
    Q3a_sol_p = [Q3a_sol[0] * x ** 2 + Q3a_sol[1] * x + Q3a_sol[2] for x in x_arr]    
    if PLOT:
        plt.plot(x_arr, y_arr, x_arr, Q3a_sol_p)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Q3a")
        plt.show()
        
    print("The limitation to this approach is that it becomes very inaccurate if the array of sums for x^4, x^3, etc. are not invertible or hard to determine accurately, then the polynomial will blow up. Futher, the polynomial will be very inaccurate if the determinant of A is very small or very large.")
    
    Q3b_sol = Q3b(x_arr, y_arr)
    Q3b_sol_p = [Q3b_sol[0] * x ** 2 + Q3b_sol[1] * x + Q3b_sol[2] for x in x_arr]  
    if PLOT:
        plt.plot(x_arr, y_arr, x_arr, Q3b_sol_p)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Q3a")
        plt.show()
    
    
    

if __name__=="__main__":
	main()