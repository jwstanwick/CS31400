def f(x):
    return x**3 - 4*x - 9

def df(x):
	return 3*x**2 - 4
    
def main():
    x = 2
    for i in range(5):
        print('Iteration ' + str(i) + ':')
        print('Current value: ' + str(x))
        print('f(x): ' + str(f(x)))
        print('df(x): ' + str(df(x)))
        print('Error: ' + str(abs(x - 2.707)))
        print('\n')
        
        x = x - f(x)/df(x)

if __name__ == "__main__":
    main()