# 35. Combine Pandas and Matplotlib: read a small CSV of monthly expenses into a DataFrame, group by category, and plot the totals as a pie chart.
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("expenses.csv")
totals=df.groupby("category")["amount"].sum()
plt.pie(totals,labels=totals.index,autopct="%1.1f%%")
plt.show()