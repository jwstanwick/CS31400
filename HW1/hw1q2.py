# Problem Statement:
# 2. (20 points) Changing the scenario in Problem 1, we now assume that you can change your direction as
# well. Your run for a fixed period of time (say, dt). After this, you re-evaluate your direction to pick the
# best direction from that instant. You keep running in this manner. How long before you get caught? Plot
# the trajectories for this case for dt = 0.1s. All other parameters stay the same. Highlight changes in
# equations from solution to problem 1.

from copy import deepcopy
from math import cos, degrees, dist, radians, sin, sqrt
from math import atan2
from time import sleep
from utils import PRINT_DEBUG, create_plot
import numpy as np


D = 25
DT = 0.1
DEBUG = False
DEATH_DISTANCE = 0.5

def find_best_player_angle(old_player, old_raptors):
	final_time = -1
	final_angle = -1
	for init_angle in range(0, 359):
		new_player = {
			"position": deepcopy(old_player["position"]),
			"velocity": deepcopy(old_player["velocity"]),
			"acceleration": deepcopy(old_player["acceleration"]),
			"angle": init_angle,
		}
   
		raptors = []
		for raptor in old_raptors:
			raptors.append({
				"position": deepcopy(raptor["position"]),
				"velocity": deepcopy(raptor["velocity"]),
				"acceleration": deepcopy(raptor["acceleration"]),
				"angle": calc_angle(raptor["position"], new_player["position"]),
			})
  
		time = 0
		while(True):
			new_player = increment_object(new_player)
			for raptor in raptors:
				raptor["angle"] = calc_angle(raptor["position"], new_player["position"])
				raptor = increment_object(raptor)			
			
			if is_dead(new_player, raptors):
				if(time > final_time):
					final_time = round(time, 3)
					final_angle = init_angle
				break
			else:
				time += DT
	if DEBUG:
		print("Best found angle is {a}".format(a=final_angle))
  
	return final_angle
 
def calc_angle(pos1, pos2):
	dx = pos2[0] - pos1[0]
	dy = pos2[1] - pos1[1]
	theta = atan2(dy, dx)
	return round(degrees(theta))

def increment_object(obj):
	obj["position"][0] += round(obj["velocity"] * cos(radians(obj["angle"])) * DT, 2)
	obj["position"][1] += round(obj["velocity"] * sin(radians(obj["angle"])) * DT, 2)
	return obj

def is_dead(player, raptors):
	for raptor in raptors:
		if dist(player["position"], raptor["position"]) < DEATH_DISTANCE:
			return True
	return False

def main():
	r0 = {
		"position": [D,0],
		"velocity": 10,
		"acceleration": 0,
		"angle": 0,
	}
	r1 = {
		"position": [-D/2, D*sqrt(3)/2],
		"velocity": 15,
		"acceleration": 0,
		"angle": 0,
	}
	r2 = {
		"position": [-D/2, -D*sqrt(3)/2],
		"velocity": 12,
		"acceleration": 0,
		"angle": 0,
	}
	raptors = [r0, r1, r2]
	player = {
		"position": [0,0],
		"velocity": 7,
		"acceleration": 0,
		"angle": 0,
	}
	time = 0
	player_positions = []
	r0_positions = []
	r1_positions = []
	r2_positions = []
	while not is_dead(player, raptors):
		player_positions.append(deepcopy(player["position"]))

		player["angle"] = find_best_player_angle(player, raptors)
		player = increment_object(player)
		
		temp_raptor_positions = []
		for raptor in raptors:
			temp_raptor_positions.append(deepcopy(raptor["position"]))
			raptor["angle"] = calc_angle(raptor["position"], player["position"])
			raptor = increment_object(raptor)
		r0_positions.append(temp_raptor_positions[0])
		r1_positions.append(temp_raptor_positions[1])
		r2_positions.append(temp_raptor_positions[2])	
  
		time += DT
	create_plot(player_positions, r0_positions, r1_positions, r2_positions, 'Homework 1, Question 2; Final Time: ' + str(round(time, 3)) + ' Seconds')
	print("Best Time: {t}".format(t=round(time, 2)))

if __name__ == "__main__":
	main()
