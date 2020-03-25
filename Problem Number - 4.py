import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

#Robot Parameters 
r = 2.0
l = 5.0  
dt  = 2
Tend = 1800.0

#Sampling Rate
N = int(Tend/dt)

v = 1.0
k1 = 2.0
k2 = 0.2

#points to be reach 
xend = [0, 100, 200, 300, 400, 500, 400,300, 200,   100,  0, 0]
yend = [0, 100, 0, -100, 0, 100, 200,   300, 300,   200,  100, 0] #all points are in  meters
   
#Blank Array   
x = np.zeros(N)
y = np.zeros(N)
th = np.zeros(N)
A = np.zeros(N)
B = np.zeros(N)
C = np.zeros(N)

k = 3    
i = 0
for k in range(12):
    if k == 1:
        
        while(i<N-1): #gradual increase included 
            th_err = math.atan2(yend[k] - y[i], xend[k] - x[i]) - th[i] #orientation error 
            d1 = abs(x[i] - xend[k])
            d2 = abs(y[i] - yend[k])
            w = v
            d = math.sqrt(d1*d1+d2*d2) #linear dist 
            if (d<0.2): break
            w1 = (w + k1*th_err)
            w2 = (w - k1*th_err)
            if (d<10):
                w1, w2 = k2*d*(w + k1*th_err), k2*d*(w - k1*th_err)
            dx = (r*dt/2.0)*(w1+w2)*math.cos(th[i])
            dy = (r*dt/2.0)*(w1+w2)*math.sin(th[i])
            dth = (r*dt/(2.0*l))*(w1-w2)
            x[i+1] = x[i] + dx
            y[i+1] = y[i] + dy
            th[i+1] = th[i] + dth    
            i = i+1
    elif k == 12:  #gradual decrease included 
        while(i<N-1):
            th_err = math.atan2(yend[k] - y[i], xend[k] - x[i]) - th[i] #orientation error 
            d1 = abs(x[i] - xend[k])
            d2 = abs(y[i] - yend[k])
            w = v
            d = math.sqrt(d1*d1+d2*d2) #linear dist 
            if (d<0.2): break
            w1 = k2*d*(w + k1*th_err)
            w2 = k2*d*(w - k1*th_err)

            dx = (r*dt/2.0)*(w1+w2)*math.cos(th[i])
            dy = (r*dt/2.0)*(w1+w2)*math.sin(th[i])
            dth = (r*dt/(2.0*l))*(w1-w2)
            x[i+1] = x[i] + dx
            y[i+1] = y[i] + dy
            th[i+1] = th[i] + dth    
            i = i+1
    else:      #constant speed
        while(i<N-1):
            th_err = math.atan2(yend[k] - y[i], xend[k] - x[i]) - th[i] #orientation error 
            d1 = abs(x[i] - xend[k])
            d2 = abs(y[i] - yend[k])
            w = v
            d = math.sqrt(d1*d1+d2*d2) #linear dist 
            if (d<0.2): break
            w1 = w + k1*th_err
            w2 = w - k1*th_err
            if (d<10):
                w1, w2 = k2*d*(w + k1*th_err), k2*d*(w - k1*th_err)
            dx = (r*dt/2.0)*(w1+w2)*math.cos(th[i])
            dy = (r*dt/2.0)*(w1+w2)*math.sin(th[i])
            dth = (r*dt/(2.0*l))*(w1-w2)
            x[i+1] = x[i] + dx
            y[i+1] = y[i] + dy
            th[i+1] = th[i] + dth    
            i = i+1


#Plot the path 
plt.xlabel(' X- Axis ')
plt.ylabel(' Y- Axis ')
plt.title(' Path of The Robot ')
plt.plot(x,y, 'ro')
plt.show()
