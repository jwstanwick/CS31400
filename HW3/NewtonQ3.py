from math import sqrt

def f(x):
    return x**3 - 4*x + 3

def df(x):
	return 3*x**2 - 4

TRUE_VALUE = (-1/2)-(sqrt(13)/2)
NUM_ITERATIONS = 5

def main():
    x = -3
    error = 1000 
    while error > 10 ** -4:
        error = abs(x - TRUE_VALUE)
        print('Current value: ' + str(x))
        print('f(x): ' + str(f(x)))
        print('df(x): ' + str(df(x)))
        print('Error: ' + str(abs(x - TRUE_VALUE)))
        print('\n')
        x = x - f(x)/df(x)


if __name__ == "__main__":
    main()