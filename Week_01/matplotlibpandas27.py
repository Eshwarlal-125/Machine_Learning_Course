# 27. Plot y=sin(x) and y=cos(x) on the same figure for x from 0 to 2π using np.linspace(); include a legend distinguishing the two curves.
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi,100)
plt.plot(x,np.sin(x),label="sin(x)")
plt.plot(x,np.cos(x),label="cos(x)")
plt.legend()
plt.show()