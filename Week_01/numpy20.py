# 20. Create a 4x4 matrix using np.arange().reshape() and compute its transpose, determinant, and inverse (if invertible).
import numpy as np
A=np.arange(1,17).reshape(4,4)
print(A.T)
print(np.linalg.det(A))
if np.linalg.det(A)!=0:
    print(np.linalg.inv(A))