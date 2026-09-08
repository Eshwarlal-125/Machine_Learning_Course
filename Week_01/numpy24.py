# 24. Write a function that accepts a 2D NumPy array and returns True if the array is symmetric (equal to its transpose), otherwise False.
import numpy as np
def is_symmetric(arr):
    return np.array_equal(arr,arr.T)

arr=np.array([[1,2,3],[2,4,5],[3,5,6]])
print(is_symmetric(arr))