import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker, cm 
from matplotlib import colors
from matplotlib.ticker import LogFormatter 
  
m = np.arange(1.0,11.0,1)           #m modes
R = np.arange(24.0,36.0,0.1)       #RoC mirror
  
# Creating 2-D grid of features

r1 = 0.998                          #R of mirror
r2 = 0.990
L = 9.1                             #length of cav                                                 
g = 1-(L/R)                         #g
F = (np.pi*((r1*r2)**0.25))/(1-(r1*r2)**0.5)    #Finesse

print("F",F)
#print("G",g)
[X, Y] = np.meshgrid(m, R)
  
fig, ax = plt.subplots(1,1)
  
#relative to fun HOM

Z= 1/((1+((2*F/np.pi)**2)*(np.sin(X*np.arccos((1-L/Y)**0.5)))**2)**0.5)  

# plots filled contour plot
  
ax.set_title('RoC vs TEM')
ax.set_xlabel('TEM (m)')
ax.set_ylabel('RoC ')
ax.set_xticks([1,2,3,4,5,6,7,8,9,10])
ax.axhline(y = 31.6, color = 'r', linestyle = 'dashed')
ax.axhline(y = 34, color = 'b', linestyle = 'dashed')    

#plt.show()
im = plt.imshow(Z, extent=[1, 10, 24, 36], origin='lower',cmap=cm.rainbow, norm=colors.LogNorm(), alpha=0.5)
formatter = LogFormatter(10, labelOnlyBase=False) 

cb = plt.colorbar(im, ax=ax)
plt.show()
