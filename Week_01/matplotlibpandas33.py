# 33. Given a DataFrame with a 'date' column and a 'sales' column, sort by date and plot sales over time using Pandas' built-in .plot() method.
import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame({"date":["2026-03-03","2026-03-01","2026-03-02"],"sales":[300,200,250]})
df["date"]=pd.to_datetime(df["date"])
df=df.sort_values("date")
df.plot(x="date",y="sales")
plt.show()