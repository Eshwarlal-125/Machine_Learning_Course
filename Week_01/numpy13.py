# 13. Given a NumPy array of 25 random integers between 1 and 100, find the sum, mean, and standard deviation.
import numpy as np
arr=np.random.randint(1,101,25)
print(arr.sum())
print(arr.mean())
print(arr.std())