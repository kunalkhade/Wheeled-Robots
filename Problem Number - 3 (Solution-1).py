import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

#Sampling Rate
N = 100
t0 = 0.0
t1 = 5.0
#Time Interval 
t = np.linspace(t0, t1, N)
dt = (t1-t0)/N

one = np.ones((N))
xp = np.ones((N))
yp = np.ones((N))
th = np.ones((N))

#Robot Parameters 
r = 20.0
L = 12.0
dotphi1 = 0.25*t*t
dotphi2 = 0.5*t

#Create an empty array in order to store values 
xp[0] = 0.0
yp[0] = 0.0
th[0] = 0.0


for i in range(N-1):
		xp[i+1] = xp[i] + (r*dt/2.0)*(dotphi1[i] + dotphi2[i])*math.cos(th[i])
		yp[i+1] = yp[i] + (r*dt/2.0)*(dotphi1[i] + dotphi2[i])*math.sin(th[i])
		th[i+1] = th[i] + (r*dt/(2.0*L))*(dotphi1[i] - dotphi2[i])

#Plot all the points
plt.xlabel(' X Direction ')
plt.ylabel(' Y Direction ')
plt.title(' DD Wheel Drive Path ')
plt.xlim(-20,100)
plt.ylim(-20,70)
plt.plot(xp,yp, 'bo')
plt.show()