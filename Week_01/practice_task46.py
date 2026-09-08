# 46. Sort a DataFrame of products by price in descending order and print the top 3 most expensive products.
import pandas as pd
df=pd.DataFrame({"product":["Laptop","Phone","Tablet","Monitor","Keyboard"],"price":[100000,80000,50000,30000,10000]})
result=df.sort_values("price",ascending=False)
print(result.head(3))