# 35. Plot y = x^2 for x from -10 to 10 using NumPy's linspace() and Matplotlib's plot(); label the axes and add a title.
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10,100)
y=x**2
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y=x^2")
plt.show()