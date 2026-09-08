# 21. Given two NumPy 1D arrays representing vectors, compute their dot product manually with a loop and verify it against np.dot().
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
dot=0
for i in range(len(a)):
    dot+=a[i]*b[i]
print(dot)
print(np.dot(a,b))