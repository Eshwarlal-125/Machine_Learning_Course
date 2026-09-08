# 15. Create two NumPy arrays of shape (3,3) and demonstrate the difference between element-wise multiplication (*) and matrix multiplication (@).
import numpy as np
A=np.arange(1,10).reshape(3,3)
B=np.arange(9,0,-1).reshape(3,3)
print(A*B)
print(A@B)