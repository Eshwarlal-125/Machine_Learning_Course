# 36. Create a figure with two line plots (sin(x) and cos(x)) on the same axes, each with a distinct color and a legend.
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi,100)
plt.plot(x,np.sin(x),color="blue",label="sin(x)")
plt.plot(x,np.cos(x),color="red",label="cos(x)")
plt.legend()
plt.show()