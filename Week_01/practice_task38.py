# 38. Generate 1,000 random numbers using np.random.randn() and plot a histogram with 20 bins.
import numpy as np
import matplotlib.pyplot as plt
data=np.random.randn(1000)
plt.hist(data,bins=20)
plt.show()