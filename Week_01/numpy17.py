# 17. Write NumPy code to normalize an array (scale all values to the range 0-1) using the formula (x - min) / (max - min).
import numpy as np
arr=np.array([10,20,30,40,50])
normalized=(arr-arr.min())/(arr.max()-arr.min())
print(normalized)