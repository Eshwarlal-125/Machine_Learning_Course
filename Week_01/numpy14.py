# 14. Given a 2D NumPy array of shape (4,4), extract the diagonal elements using np.diag() and compute their sum.
import numpy as np
arr=np.arange(1,17).reshape(4,4)
diagonal=np.diag(arr)
print(diagonal)
print(diagonal.sum())