import matplotlib.pyplot as plt
import numpy as np
import math

def time(seconds=10, granularity=1):
	i = 0
	time = []
	while (i < seconds):
		time.append(i)
		i+=granularity
	return time


pos = np.array([0,0])
vel = np.array([1,0])

exp_path = np.array([[i, math.sin(i)] for i in time(10, 0.01) ])

for i in time(1, 1):
	pos = vel*i

print (pos)

# plt.plot(exp_path[:, 0], exp_path[:, 1])
# plt.show()