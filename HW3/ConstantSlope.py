def f(x):
	return x**3 - 4*x - 9

def df(x):
    return 8
	# return 3*x**2 - 4

def main():
	cur = 2
	for i in range(4):
		print('Iteration ' + str(i) + ':')
		print('Current value: ' + str(cur))
		print('f(x): ' + str(f(cur)))
		print('df(x): ' + str(df(cur)))
		print('Iteration Value: ' + str(f(cur)/df(cur)))
		print('\n')
  
		cur = cur - f(cur)/df(cur)
	
if __name__ == "__main__":
	main()