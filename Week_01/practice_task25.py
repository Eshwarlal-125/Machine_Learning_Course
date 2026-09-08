# 25. Given a 1D array of 20 elements, reshape it into a 4x5 matrix, then extract the 2nd and 3rd columns.
import numpy as np
arr=np.arange(1,21).reshape(4,5)
print(arr)
print(arr[:,1:3])