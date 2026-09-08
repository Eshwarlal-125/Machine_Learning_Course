# 40. Plot a pie chart showing the percentage breakdown of a monthly budget across 4 categories, and save the figure as budget.png.
import matplotlib.pyplot as plt
categories=["Rent","Food","Transport","Other"]
budget=[50,20,15,15]
plt.pie(budget,labels=categories,autopct="%1.1f%%")
plt.title("Monthly Budget")
plt.savefig("budget.png")
plt.show() 