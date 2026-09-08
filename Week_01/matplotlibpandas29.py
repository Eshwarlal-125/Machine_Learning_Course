# 29. Generate a histogram of 500 normally distributed random numbers and overlay a vertical line at the mean using plt.axvline().
import numpy as np
import matplotlib.pyplot as plt
data=np.random.randn(500)
mean=data.mean()
plt.hist(data,bins=20)
plt.axvline(mean)
plt.show()