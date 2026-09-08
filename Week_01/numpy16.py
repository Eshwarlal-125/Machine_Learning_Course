# 16. Given a NumPy array representing daily temperatures for a month, use boolean masking to find all days with temperature above 35°C and count them.
import numpy as np
temp=np.array([32,36,38,30,40,34,37,31,35,39])
hot=temp[temp>35]
print(hot)
print(len(hot))