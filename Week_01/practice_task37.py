# 37. Given a list of 7 daily temperatures, plot a bar chart with the day names on the x-axis and temperatures on the y-axis.
import matplotlib.pyplot as plt
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
temp=[25,28,27,30,29,31,26]
plt.bar(days,temp)
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()