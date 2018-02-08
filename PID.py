import numpy as np
import matplotlib.pyplot as plt


#TRY EXPERIMENTING WITH K VALUES
##################################

kp = 0.1
kd = 0.0
ki = 0.0							

##################################


# PLAY WITH POSITION AND VELOCITY
pos = np.array([0,0])
vel = np.array([3,5])


#FUNCTION GENERATOR (USE ANY ONE)
##################################

#LINEAR FUNCTION
func = np.array([[i, i] for i in range(100)]) 

#QUADRATIC FUNCTION
#func = np.array([[i, (i**2)] for i in range(100)])

# SIN CURVE
#func = np.array([[i, np.sin(i)] for i in range(100)])

# COS CURVE
# func = np.array([[i, np.cos(i)] for i in range(100)])

##################################



# DONT TOUCH THESE UNLESS YOU KNOW WHAT YOURE DOING
x = [pos[0]]
y = [pos[1]]

last_err = 0.0
sum_err = 0.0

for i in range(100):
	pos = pos + vel

	err = func[i] - pos
	sum_err += err
	correction = err*kp + (err-last_err)*kd + sum_err*ki
	last_err = err

	vel = vel + correction

	x.append(pos[0])
	y.append(pos[1])


plt.plot(func[:,0],func[:,1])
plt.plot(x,y)
plt.show()