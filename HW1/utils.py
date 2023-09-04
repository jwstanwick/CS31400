import matplotlib.pyplot as plt

def PRINT_DEBUG(raptors, player):
	print("player object: ", player)
	for index, raptor in enumerate(raptors):
		print("raptor {i}: {x}".format(i=index, x=raptor))
  
def create_plot(player_positions, r0_positions, r1_positions, r2_positions, plot_title):
	player_x = []
	player_y = []
	for coord in player_positions:
		player_x.append(coord[0])
		player_y.append(coord[1])
	
	r0_x = []
	r0_y = []
	for coord in r0_positions:
		r0_x.append(coord[0])
		r0_y.append(coord[1])
  
	r1_x = []
	r1_y = []
	for coord in r1_positions:
		r1_x.append(coord[0])
		r1_y.append(coord[1])
  
	r2_x = []
	r2_y = []
	for coord in r2_positions:
		r2_x.append(coord[0])
		r2_y.append(coord[1])
	
	plt.plot(player_x, player_y)
	plt.plot(r0_x, r0_y)
	plt.plot(r1_x, r1_y)
	plt.plot(r2_x, r2_y)
	plt.legend(['Player', 'Raptor 0', 'Raptor 1', 'Raptor 2'])
	plt.ylabel('Y Position')
	plt.xlabel('X Position')
	plt.title(plot_title)
	plt.show()
	return