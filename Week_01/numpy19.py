# 19. Use np.where() to replace all even numbers in a NumPy array with -1 and keep odd numbers unchanged.
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
result=np.where(arr%2==0,-1,arr)
print(result)