# 27. Write code to reverse a 1D NumPy array both using slicing ([::-1]) and np.flip().
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr[::-1])
print(np.flip(arr))