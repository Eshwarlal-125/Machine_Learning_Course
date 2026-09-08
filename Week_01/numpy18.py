# 18. Given a 2D array of shape (5,3) representing 5 students' marks in 3 subjects, compute the total and average marks per student using axis-based aggregation.
import numpy as np
marks=np.array([[80,70,90],[60,75,85],[90,85,95],[70,65,80],[88,92,84]])
print(marks.sum(axis=1))
print(marks.mean(axis=1))