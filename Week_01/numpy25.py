# 25. Stack three NumPy arrays of shape (2,2) using np.vstack() and np.hstack(); print the resulting shapes and explain the difference.
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
c=np.array([[9,10],[11,12]])
v=np.vstack((a,b,c))
h=np.hstack((a,b,c))
print(v)
print(v.shape)
print(h)
print(h.shape)