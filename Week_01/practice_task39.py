# 39. Create a 1x3 subplot grid showing a line plot, a bar chart, and a scatter plot of related data, with a shared figure title.
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,6,8,10]
fig,ax=plt.subplots(1,3)
ax[0].plot(x,y)
ax[1].bar(x,y)
ax[2].scatter(x,y)
fig.suptitle("Related Data")
plt.show()