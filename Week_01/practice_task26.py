# 26. Create a 6x6 array using np.arange().reshape() and extract the middle 4x4 sub-array using slicing.
import numpy as np
arr=np.arange(1,37).reshape(6,6)
print(arr)
print(arr[1:5,1:5])