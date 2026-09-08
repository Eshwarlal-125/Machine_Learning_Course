# 29. Given a 1D array of 15 exam scores, compute the mean, median, standard deviation, and identify scores above the mean using boolean masking.
import numpy as np
scores=np.array([65,78,90,55,88,72,95,60,84,70,92,68,81,75,85])
mean=np.mean(scores)
print(mean)
print(np.median(scores))
print(np.std(scores))
print(scores[scores>mean])