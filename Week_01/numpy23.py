# 23. Given a NumPy array of shape (3,4), use fancy indexing to select rows [0,2] and columns [1,3] simultaneously.
import numpy as np
arr=np.arange(1,13).reshape(3,4)
result=arr[[0,2]][:,[1,3]]
print(result)