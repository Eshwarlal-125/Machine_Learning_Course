# 33. Create a 4x4 matrix, compute its transpose, determinant, and inverse (verify A @ inv(A) ≈ Identity).
import numpy as np
A=np.array([[1,2,3,4],[2,5,7,1],[3,1,6,2],[4,2,1,8]])
print(A.T)
print(np.linalg.det(A))
inv=np.linalg.inv(A)
print(inv)
print(np.allclose(A@inv,np.eye(4)))