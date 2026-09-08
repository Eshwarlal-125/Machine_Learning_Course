# 31. Given a 2D array representing students (rows) and 3 subjects (columns), compute each student's average using axis=1 and each subject's average using axis=0.
import numpy as np
marks=np.array([[80,70,90],[60,75,85],[90,85,95]])
print(np.mean(marks,axis=1))
print(np.mean(marks,axis=0))