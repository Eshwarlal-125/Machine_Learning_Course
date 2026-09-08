# 12. Using NumPy, create a 6x6 identity matrix and replace its diagonal with the values [1,2,3,4,5,6].
import numpy as np
arr=np.eye(6)
np.fill_diagonal(arr,[1,2,3,4,5,6])
print(arr)