# 22. Write a program combining Python and NumPy: read 10 numbers from user input into a list, convert to a NumPy array, and print the sorted array along with its median.
import numpy as np
numbers=list(map(int,input("Enter 10 numbers: ").split()))
arr=np.array(numbers)
print(np.sort(arr))
print(np.median(arr))