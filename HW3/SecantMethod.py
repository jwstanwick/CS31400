def main():
	def f(x):
		return x**3 - 4*x - 9
	
	x_prev = 2
	x  = 3
	for i in range(5):  
		print('Iteration ' + str(i) + ':')
		print('Current value: ' + str(x))
		print('Previous value: ' + str(x_prev))
		print('(x - x_prev))/(f(x) - f(x_prev): ' + str((f(x) * (x - x_prev))/(f(x) - f(x_prev))))
		print('Error: ' + str(abs(x - 2.707)))
		print('\n')
  
		next_x = x - (f(x) * (x - x_prev))/(f(x) - f(x_prev))
		x_prev = x
		x = next_x
	return

if __name__ == "__main__":
	main()