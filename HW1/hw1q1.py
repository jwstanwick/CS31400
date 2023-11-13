# Problem Statement:
#  1. (10 points) In this problem, there are three raptors, denoted by r0, r1 and r2, at the corner of an
# equilateral triangle and you are standing in the middle. Specifically, we assume the coordinates of r0, r1
# and r2 are (d, 0), (−d/2, d√3/2) and (−d/2, −d√3/2), respectively. Your coordinate is (0, 0). That is, the
# distance between you and any of the raptors is d meters. The raptors all run towards you at different
# speeds with r0, r1 and r2 being 10 m/s, 15 m/s and 12 m/s, respectively. Your speed is 7 m/s. Assume
# that you only pick your direction in the beginning (it cannot be changed after the initial selection). Find
# the direction that maximizes your survival time. What is the optimal direction (to within a degree) and
# how long before you get eaten by one of the raptors. For this case, also show the plot of all entities and
# their movement. Show the plot for d = 25 for the best angle, and print the time. Also, write the
# equations governing the movement of raptors.

from copy import deepcopy
from math import cos, degrees, dist, radians, sin, sqrt
from math import atan2
from time import sleep
from utils import PRINT_DEBUG, create_plot
import numpy as np
import matplotlib.pyplot as plt

D = 25
DT = 0.1
DEBUG = False
DEATH_DISTANCE = 15 * DT

DEFAULT_OBJECT_PROPERTIES = {
	"position": [0,0],
	"velocity": 0,
 	"acceleration": 0,
	"angle": 0,
}

def calc_angle(pos1, pos2):
	dx = pos2[0] - pos1[0]
	dy = pos2[1] - pos1[1]
	theta = atan2(dy, dx)
	return round(theta)

def increment_object(obj):
	obj["position"][0] += round(obj["velocity"] * cos(obj["angle"]) * DT, 1)
	obj["position"][1] += round(obj["velocity"] * sin(obj["angle"]) * DT, 1)
	return obj

def is_dead(player, raptors):
	for raptor in raptors:
		if dist(player["position"], raptor["position"]) < DEATH_DISTANCE:
			return True
	return False

def main():
	final_time = -1
	final_angle = -1
	player_positions = []
	r0_positions = []
	r1_positions = []
	r2_positions = []
	for init_angle in range(0, 359):
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
			"angle": radians(init_angle),
		}

		time = 0
		write_player_positions = []
		write_raptor_positions = []
		while(True):
			write_player_positions.append(deepcopy(player["position"]))
			player = increment_object(player)

			temp_raptor_positions = []
			for raptor in raptors:
				temp_raptor_positions.append(deepcopy(raptor["position"]))
				raptor["angle"] = calc_angle(raptor["position"], player["position"])
				raptor = increment_object(raptor)
			write_raptor_positions.append(temp_raptor_positions)
			
			if is_dead(player, raptors):
				if DEBUG:
					print("Dead at {t} seconds and {a} angle".format(t=time, a=init_angle))
					sleep(DT)

				if(time > final_time):
					final_time = round(time, 3)
					final_angle = init_angle
					r0_positions = []
					r1_positions = []
					r2_positions = []
					for x in write_raptor_positions:
						r0_positions.append(x[0])
						r1_positions.append(x[1])
						r2_positions.append(x[2])
					player_positions = write_player_positions
				break
			else:
				time += DT

	create_plot(player_positions, r0_positions, r1_positions, r2_positions, 'Homework 1, Question 1\nFinal Time: ' + str(round(final_time, 3)) + ' Seconds; Final Angle: ' + str(final_angle) + ' Degrees')
	print("Best Time: {t}, Best Angle: {a}".format(t=final_time, a=final_angle))

if __name__ == "__main__":
	main()
