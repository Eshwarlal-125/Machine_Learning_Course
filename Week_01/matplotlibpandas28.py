# 28. Create a bar chart comparing the average marks of 4 subjects, with a distinct color for the highest-scoring subject.
import matplotlib.pyplot as plt
subjects=["Math","Physics","CS","English"]
marks=[85,78,92,80]
colors=["blue","blue","red","blue"]
plt.bar(subjects,marks,color=colors)
plt.show()