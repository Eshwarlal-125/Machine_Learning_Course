# 30. Create a 2x2 grid of subplots showing four different chart types (line, bar, scatter, histogram) from the same dataset.
import matplotlib.pyplot as plt
data=[1,2,3,4,5]
fig,ax=plt.subplots(2,2)
ax[0,0].plot(data)
ax[0,1].bar(range(5),data)
ax[1,0].scatter(range(5),data)
ax[1,1].hist(data)
plt.show()