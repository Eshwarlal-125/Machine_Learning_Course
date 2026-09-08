# 28. Create two 3x3 matrices of random integers and compute their element-wise sum, product, and matrix product (@).
import numpy as np
A=np.random.randint(1,10,(3,3))
B=np.random.randint(1,10,(3,3))
print(A)
print(B)
print(A+B)
print(A*B)
print(A@B)