from math import sqrt


def f(x):
    return x**2 - 12

def df(x):
	return 2*x
    
def main():
    x = 3
    NUM_ITERATIONS = 5
    error = [0] * NUM_ITERATIONS
    for i in range(NUM_ITERATIONS):
        print('Iteration ' + str(i) + ':')
        print('Current value: ' + str(x))
        print('f(x): ' + str(f(x)))
        print('df(x): ' + str(df(x)))
        print('Error: ' + str(abs(x - sqrt(12))))
        error[i] = abs(x - sqrt(12))
        if i > 0:
            print('Error Ratio: ' + str(error[i]/(error[i-1]**2)))
            
        print('\n')
        x = x - f(x)/df(x)


if __name__ == "__main__":
    main()