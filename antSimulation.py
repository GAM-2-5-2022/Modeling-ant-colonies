import numpy as np
args = {"a":10, "b":1} #[food_coefficient, colony_coefficient]
state_0 = [2, 2] #[food, colony]

def food_d(colony, a):return -a*colony #the food will decrease more the bigger the colony is. (added coefficient a)
def colony_d(food, b):return b*food #the colony will increase more the bigger the food supply is. (added coefficient b)
d_state = [food_d, colony_d]


def state(t, dt, state_0, d_state, args):
	state_n = state_0
	x_range = [state_0[0]]
	y_range = [state_0[1]]
	print(args)
	for n in np.arange(0, t, dt):
		#this finds the derivatives at the points described in the state_n array
		d_x, d_y = [d_state[0](state_n[1], args["a"]), d_state[1](state_n[0], args["b"])] 

		# only uncomment this if you dont care about your terminal
		# print(state_n)

		#changes the states and adds them to a arrays for plotting in matplotlib
		state_n[0] += d_x*dt 
		state_n[1] += d_y*dt
		x_range.append(state_n[0])
		y_range.append(state_n[1])
	
	return [x_range, y_range]

food, colony = state(10, 0.001, state_0, d_state, args)
print("max COLONY: " + str(max(colony)) + ", max FOOD: " + str(max(food)))
print("min COLONY: " + str(min(colony)) + ", min FOOD: " + str(min(food)))

def writeDataToFile(arr1,label1, arr2, label2):
	f = open("./results.txt", "w")
	for i in range(0, int(np.round(len(arr1)/10,0))):
		f.write(f"{label1}: {arr1[10*i]}, {label2}: {arr2[10*i]} \n")
	f.write(f"{label1}: {arr1[-1]}, {label2}: {arr2[-1]}")
	f.close()

writeDataToFile(food,"FOOD",colony,"COLONY")
