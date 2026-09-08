# 24. Create a 5x5 array of random integers between 10 and 50; print its maximum and minimum values.
import numpy as np
arr=np.random.randint(10,51,(5,5))
print(arr)
print(arr.max())
print(arr.min())