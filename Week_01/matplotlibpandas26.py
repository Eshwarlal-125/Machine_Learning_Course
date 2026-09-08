# 26. Given a NumPy array of 30 days of temperature readings, plot a line chart with the day number on the x-axis and temperature on the y-axis, including a title and axis labels.
import numpy as np
import matplotlib.pyplot as plt
temp=np.random.randint(20,40,30)
days=np.arange(1,31)
plt.plot(days,temp)
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Daily Temperature")
plt.show()