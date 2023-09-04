from copy import deepcopy
from venv import create
import matplotlib.pyplot as plt
# 3. (40 points) In this problem, there is only one 
# raptor, which is on the same line as you (say, x-axis).
# The raptor spots you 50 meters away and runs towards 
# you, accelerating at 4.5 m/s2 up to its maximum
# speed of 20 m/s. You run with an acceleration of 2.5 m/
# s2 and your maximum speed is 9 m/s. How long
# before you get caught? Write a Matlab/ Python program to 
# simulate this process.
INIT_DIST = 50
RAPTOR_ACCELERATION = 4.5
RAPTOR_MAX_SPEED = 20
PLAYER_ACCELERATION = 2.5
PLAYER_MAX_SPEED = 9
DT = 0.1
DEATH_DISTANCE = 0.1

def update_velocity(obj):
	if obj["velocity"] < obj["max_speed"]:
		obj["velocity"] += obj["acceleration"] * DT
	if obj["velocity"] > obj["max_speed"]:
		obj["velocity"] = obj["max_speed"]
	return obj

def update_position(obj):
	obj["position"] += obj["velocity"] * DT
	return obj

def is_dead(player, raptor):
	if abs(player["position"] - raptor["position"]) < DEATH_DISTANCE or raptor["position"] > player["position"]:
		return True
	return False

def create_plot_q3(player_positions, raptor_positions, plot_title):
	player_x = []
	player_y = []
	for coord in player_positions:
		player_x.append(coord)
		player_y.append(0)
	
	raptor_x = []
	raptor_y = []
	for coord in raptor_positions:
		raptor_x.append(coord)
		raptor_y.append(0)
	
	plt.plot(player_x, player_y)
	plt.plot(raptor_x, raptor_y)
	plt.legend(['Player', 'Raptor'])
	plt.ylabel('Y Position')
	plt.xlabel('X Position')
	plt.title(plot_title)
	plt.show()
	return

def main():
	raptor = {
		"position": 0,
		"velocity": 0,
		"acceleration": RAPTOR_ACCELERATION,
  		"max_speed": RAPTOR_MAX_SPEED,
	}
	player = {
		"position": INIT_DIST,
		"velocity": 0,
		"acceleration": PLAYER_ACCELERATION,
		"max_speed": PLAYER_MAX_SPEED,
	}

	time = 0
	raptor_positions = []
	player_positions = []
	while not is_dead(player, raptor):
		raptor_positions.append(deepcopy(raptor["position"]))
		player_positions.append(deepcopy(player["position"]))
		raptor = update_position(raptor)
		player = update_position(player)
		raptor = update_velocity(raptor)
		player = update_velocity(player)
		time = round(time + DT, 2)
  
	# create_plot_q3(player_positions, raptor_positions, 'Homework 1, Question 3; Final Time: ' + str(time) + ' Seconds')
	print("Time to death: " + str(time))
	print("Distance to death: " + str(round(player["position"], 2)))
	return 

if __name__ == "__main__":
	main()