# 32. Use np.where() to replace all negative values in an array with 0 and all positive values with 1.
import numpy as np
arr=np.array([-5,3,-2,7,0,-8,4])
result=np.where(arr<0,0,np.where(arr>0,1,arr))
print(result)