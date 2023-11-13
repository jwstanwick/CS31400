from random import randint

# Consider a roll of a biased 6-sided dice, where even numbers are twice as likely as odd numbers.
def generate_num():
	return randint(1, 9)

def simulate_dice_roll():
	num = generate_num()
	if num == 1:
		return 1
	if num == 2 or num == 3:
		return 2
	if num == 4:
		return 3
	if num == 5 or num == 6:
		return 4
	if num == 7:
		return 5
	if num == 8 or num == 9:
		return 6
	return -1

def main():
	# Simulate 1000 dice rolls
	rolls = [0] * 7
	for i in range(1000):
		rolls[simulate_dice_roll()] += 1

	# Print the results
	print("1: " + str(rolls[1]))
	print("2: " + str(rolls[2]))
	print("3: " + str(rolls[3]))
	print("4: " + str(rolls[4]))
	print("5: " + str(rolls[5]))
	print("6: " + str(rolls[6]))
 
	# Calculate mean
	mean = 0
	for i in range(1, 7):
		mean += i * rolls[i]
	mean /= 1000
	print("Mean: " + str(mean))
 
	# Calculate variance
	variance = 0
	for i in range(1, 7):
		variance += (i - mean) ** 2 * rolls[i]
	variance /= 1000
	print("Variance: " + str(variance))
 
	# Calculate standard deviation
	standard_deviation = variance ** 0.5
	print("Standard Deviation: " + str(standard_deviation))

if __name__=="__main__":
    main()