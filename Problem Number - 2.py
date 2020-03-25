import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import math


#Sampling Rate
N = 200
t0 = 0.0
t1 = 10.0

#Time Interval 
t = np.linspace(t0, t1, N)
dt = (t1-t0)/N
xp = np.ones((N))
yp = np.ones((N))
th = np.ones((N))

#Robot Parameters 
r = 0.08 
L1 = 0.30
L2 = 0.20

#Create an empty array in order to store values 
xp[0] = 0.0
yp[0] = 0.0
th[0] = 0.0


for i in range(N-1):
		ph1 = 0.75*np.cos(i/30)
		ph2 = 1.5*np.cos(i/30)
		ph3 = -1.0
		ph4 = 0.5
		A = (ph1 + ph2 + ph3 + ph4)
		B = (-ph1 + ph2 + ph3 - ph4)
		C = (-ph1 + ph2 - ph3 + ph4)
		xp[i+1] = xp[i] + (r*dt/4.0)*(A* np.cos(th[i])- B*np.sin(th[i]))
		yp[i+1] = yp[i] + (r*dt/4.0)*(A* np.sin(th[i]) + B*np.cos(th[i]))
		th[i+1] = th[i] + (r*dt/(4.0))*((1/(L1-L2)*C))

plt.scatter(xp, yp, color='g')
plt.xlabel(' X Direction ')
plt.ylabel(' Y Direction ')
plt.title(' Mechanum Wheel Drive Path ')
plt.pause(0.03)

#Plot all the points
u = 8 * np.cos(th[i])
v = 8 * np.sin(th[i])
print (xp[N-1], yp[N-1], u, v)
plt.quiver(xp[N-1],yp[N-1],u,v)
plt.savefig('mecanumpath.pdf')
plt.show()
plt.xlabel(' X Direction ')
plt.ylabel(' Y Direction ')
plt.title(' Mechanum Wheel Drive Path ')
plt.xlim(0,0.25)
plt.ylim(-0.3,0.05)
plt.quiver(xp[N-1],yp[N-1],u,v)
plt.plot(xp,yp, 'bo')
plt.show()