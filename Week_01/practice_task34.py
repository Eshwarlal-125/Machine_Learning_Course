# 34. Stack three 1D arrays of equal length vertically and horizontally; print both results and their shapes.
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.array([7,8,9])
vertical=np.vstack((a,b,c))
horizontal=np.hstack((a,b,c))
print(vertical)
print(vertical.shape)
print(horizontal)
print(horizontal.shape)