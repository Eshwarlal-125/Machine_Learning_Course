# 30. Demonstrate broadcasting by adding a (3,1) column vector to a (1,4) row vector and explain the resulting shape.
import numpy as np
column=np.array([[1],[2],[3]])
row=np.array([[10,20,30,40]])
result=column+row
print(result)
print(result.shape)