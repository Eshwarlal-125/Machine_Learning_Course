# 31. Load a small DataFrame of 6 products (name, price, quantity) and compute a new column 'total' as price × quantity.
import pandas as pd
df=pd.DataFrame({"name":["A","B","C","D","E","F"],"price":[100,200,150,300,250,400],"quantity":[2,3,1,4,2,1]})
df["total"]=df["price"]*df["quantity"]
print(df)