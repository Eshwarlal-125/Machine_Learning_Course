# 41. Create a Pandas Series of 6 monthly sales figures with month names as the index, then print the month with the highest sales.
import pandas as pd
sales=pd.Series([12000,15000,11000,18000,14000,20000],index=["Jan","Feb","Mar","Apr","May","Jun"])
print(sales.idxmax())